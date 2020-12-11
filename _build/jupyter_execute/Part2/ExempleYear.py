#!/usr/bin/env python
# coding: utf-8

# # Analyse yearly Results

# In[20]:


import plotFuncAndClass as hm
import pandas as pd
from ipywidgets import interact, interactive, fixed, interact_manual, IntSlider
# Standard plotly imports
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
# Using plotly + cufflinks in offline mode
import cufflinks as cf
cf.go_offline(connected=False)
init_notebook_mode(connected=False)


# In[21]:


listLat=['\Delta t','DNI', 'T_{amb}', '\dot{m}_{Demand}', 'T_{demand}', '\dot{m}_{SF}', 'T_{SF}', '\dot{m}_{aux}',
    '\dot{q}_{boiler}', '\dot{q}_{abs}','M_{storage}', 'T_{storage}', '\dot{m}_{Storage -> boiler}', '\dot{m}_{SF->Boiler}', '\dot{m}_{SF->Storage}']
varDescription=['Hour','Direct Normal Irradiance', 'Ambient Temperature', 'Demand Mass Flow Rate', 'Temperature Demand', 
                'Mass flow rate from the Solar Field', 'Temperature of the Solar Field', 'Auxiliar Mass flow rate', 
               'Heat From The Boiler', 'Heat absorbed by the receiver','Mass in the Storage', 'Temperature of the storage', 'Mass flow rate from the Storage to the Boiler',
               'Mass flow rate from the Solar Field to the Boiler', 'Mass flow rate from the Solar Field to the Storage']
df = pd.read_csv('data/CoSim.csv') #read a specific csv file
dfMILP= pd.read_csv('data/MILP.csv') #read another specific csv file with same fields
dfSM1= pd.read_csv('data/SM1.csv') #read another specific csv file with same fields
dfSM2= pd.read_csv('data/SM2.csv') #read another specific csv file with same fields
tabDataFrames=[df,dfSM1,dfSM2, dfMILP]
tabNameDataFrame=['CoSim','SM1','SM2','MILP','3 CoSim']
nameColumns=list(df.columns)
tabVar=[hm.nameAndUnit(nameColumns[i],nameColumns[i],varDescription[i],'',listLat[i]) for i in range(0,len(nameColumns))]


# ## Plot of Daily average values

# In[22]:


dfDaily = pd.read_csv('data/CoSimDaily.csv') #read a specific csv file
dfMILPDaily= pd.read_csv('data/MILPDaily.csv') #read another specific csv file with same fields
dfSM1Daily= pd.read_csv('data/SM1Daily.csv') #read another specific csv file with same fields
dfSM2Daily= pd.read_csv('data/SM2Daily.csv') #read another specific csv file with same fields
tabDaily=[dfDaily, dfSM1Daily, dfSM2Daily, dfMILPDaily]
nameColumnsDay=list(dfDaily.columns)
tabVarDay=[hm.nameAndUnit(nameColumnsDay[i],nameColumnsDay[i],varDescription[i],'',listLat[i]) for i in range(0,len(nameColumnsDay))]


# In[23]:


def plot1VarYear(ControlModel, var1):
    titleFunc= var1.varDescription + ' in ' + var1.unitVar
    if(ControlModel<4):
        toPlot=tabDaily[ControlModel]
        toPlot['date']=toPlot['day(d)'].map(hm.fromNumDayToDate)
        toPlot=toPlot.set_index('date')
        toPlot.iplot(mode='markers',y=var1.keyDF , title=titleFunc, xTitle='day (d)', symbol='square', size=4,
                     yTitle='$'+var1.lat+'('+var1.unitVar+')$',showlegend=True)
    else:
        toPlot=pd.concat([tabDaily[i].add_suffix('_'+tabNameDataFrame[i]) for i in range(0,3)], axis=1)
        toPlot['date']=toPlot['day(d)_CoSim'].map(hm.fromNumDayToDate)
        toPlot=toPlot.set_index('date')
        toPlot[[var1.keyDF+'_'+tabNameDataFrame[i] for i in range(0,3)]].iplot(mode='markers', symbol='square', size=4,
                                    title=titleFunc, xTitle='day (d)', yTitle='$'+var1.lat+'('+var1.unitVar+')$',showlegend=True)


# In[24]:


interactive_plot1VarYear = interactive(plot1VarYear,
                                      ControlModel=[(tabNameDataFrame[i],i) for i in range(0,5)],
                                      var1=[(tabVarDay[i].varDescription,tabVarDay[i]) for i in range(1,len(nameColumnsDay))]);
output1VarYear = interactive_plot1VarYear.children[-1]
output1VarYear.layout.height = '450px'
interactive_plot1VarYear


# In[12]:


plot1VarYear(interactive_plot1VarYear.kwargs['ControlModel'],interactive_plot1VarYear.kwargs['var1'])


# ## HeatMaps

# In[13]:


def heatMapFromVarName(var, ControlModel):
    df=tabDataFrames[ControlModel]
    nbDays= df[var.keyDF].size//24;
    data=[[df[var.keyDF][day*24+hour] for hour in range(0,24)]  for day in range(0,nbDays)];
    titleFunc = 'Heatmap of the '+var.varDescription +' in '+var.unitVar+' through the year';
    test10=pd.DataFrame(data,index = [hm.fromNumDayToDate(k) for k in range(0,nbDays)]);
    test10.iplot(kind='heatmap', title = titleFunc, colorscale ='spectral',                  showlegend=True, text=var.keyDF );


# In[14]:


interactive_plotHM = interactive(heatMapFromVarName, var=[(tabVar[i].varDescription,tabVar[i]) for i in range(1,len(nameColumns))],
                              ControlModel=[(tabNameDataFrame[i],i) for i in range(0,4)])
outputHM = interactive_plotHM.children[-1]
outputHM.layout.height = '450px'
interactive_plotHM


# In[15]:


heatMapFromVarName(interactive_plotHM.kwargs['var'],interactive_plotHM.kwargs['ControlModel']);


# In[16]:


df.corr().iplot(kind='heatmap',colorscale="Blues", title="Correlation between variables along the year",  showlegend=True)


# In[17]:


def plotRepart(var):
    toPlot=pd.concat([tabDaily[i][var.keyDF] for i in range(0,4)], axis=1)
    toPlot.columns=tabNameDataFrame[0:-1]
    toPlot.iplot(kind='box',xTitle="Control Model", yTitle = var.unitVar,
                 title=var.varDescription + ' average repartition trough the year of daily values', showlegend=False)


# In[18]:


interactive_plotBox = interactive(plotRepart, var=[(tabVarDay[i].varDescription,tabVarDay[i]) for i in range(1,len(nameColumns))])
outputHM = interactive_plotBox.children[-1]
outputHM.layout.height = '450px'
interactive_plotBox


# In[19]:


plotRepart(interactive_plotBox.kwargs['var'])

