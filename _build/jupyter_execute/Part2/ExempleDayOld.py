#!/usr/bin/env python
# coding: utf-8

# # Analysis of Hourly Values

# ## TestTitre

# ```{margin} L'équation cubique de Gausse
# Se résoud en développant en $e^{-x}$
# ```

# $$
#   \int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
# $$

# $$
#   w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
# $$ (testDolls)

# ```{math}
# :label: testIn
# w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
# ```

# - A link to an equation directive: {eq}`testIn`
# - A link to a dollar math block: {eq}`testDolls`

# In[55]:


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


# In[56]:


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


# ## Daily plotting

# In[57]:


def plot1VarDay(NHour, ControlModel, dayStart, var1):
    titleFunc= var1.varDescription + ' in ' + var1.unitVar + ' starting on ' + hm.fromNumDayToDate(dayStart)
    if(ControlModel<4):
        toPlot=tabDataFrames[ControlModel][dayStart*24:dayStart*24+NHour]
        toPlot['hourMod']=(toPlot['hour(h)']-dayStart*24)%NHour
        toPlot=toPlot.set_index('hourMod')
        
        fig = toPlot.iplot(kind='scatter',y=var1.keyDF , title=titleFunc, xTitle='hour (h)', filename="../images/test.png",
                     yTitle='$'+var1.lat+'('+var1.unitVar+')$',showlegend=True, asFigure=True)
    else:
        toPlot=pd.concat([tabDataFrames[i].add_suffix('_'+tabNameDataFrame[i]) for i in range(0,3)], axis=1)[dayStart*24:dayStart*24+NHour]
        toPlot['hourMod']=(toPlot['hour(h)_CoSim']-dayStart*24)%NHour
        toPlot=toPlot.set_index('hourMod')
        fig = toPlot[[var1.keyDF+'_'+tabNameDataFrame[i] for i in range(0,3)]].iplot(kind='scatter', asFigure=True,
                                    title=titleFunc, xTitle='hour (h)', yTitle='$'+var1.lat+'('+var1.unitVar+')$',showlegend=True)
    fig.write_image("../images/plot1VarDay.png")
    lol = fig.write_html("../images/plot1VarDay.html",include_mathjax='cdn')
    return fig


# In[58]:


interact(plot1VarDay, NHour=fixed(96),
                                      ControlModel=[(tabNameDataFrame[i],i) for i in range(0,5)],
                                      dayStart=IntSlider(min=0, max=df['hour(h)'].size//24-4, step=1, value=170),
                                      var1=[(tabVar[i].varDescription,tabVar[i]) for i in range(1,len(nameColumns))])


# In[59]:


interactive_plot1VarDay = interactive(plot1VarDay, NHour=fixed(96),
                                      ControlModel=[(tabNameDataFrame[i],i) for i in range(0,5)],
                                      dayStart=IntSlider(min=0, max=df['hour(h)'].size//24-4, step=1, value=170),
                                      var1=[(tabVar[i].varDescription,tabVar[i]) for i in range(1,len(nameColumns))])


# In[24]:


#output1VarDay


# #### Plot 2 variables on choice, 4 days range; 1 for the 3 models, the other for the coSim Models

# In[61]:


def plot2VarDay(NHour, ControlModel, dayStart, var1,var2):
    titleFunc= var1.varDescription + ' & ' + var2.varDescription + ' starting on ' + hm.fromNumDayToDate(dayStart)
    if(ControlModel<4):
        toPlot=tabDataFrames[ControlModel][dayStart*24:dayStart*24+NHour]
        toPlot['hourMod']=(toPlot['hour(h)']-dayStart*24)%NHour
        toPlot=toPlot.set_index('hourMod')
        toPlot.iplot(kind='scatter',y=var1.keyDF , secondary_y = var2.keyDF,                                                       title=titleFunc, xTitle='hour (h)', yTitle='$'+var1.lat+'('+var1.unitVar+')$',                secondary_y_title='$'+var2.lat+'('+var2.unitVar+')$', showlegend=True)
    else:
        toPlot=pd.concat([tabDataFrames[i].add_suffix('_'+tabNameDataFrame[i]) for i in range(0,3)], axis=1)[dayStart*24:dayStart*24+NHour]
        toPlot[var2.keyDF+'_CoSim']=tabDataFrames[0][var2.keyDF][dayStart*24:dayStart*24+NHour]
        toPlot['hourMod']=(tabDataFrames[0]['hour(h)'][dayStart*24:dayStart*24+NHour]-dayStart*24)%NHour
        
        testIn=toPlot[[var1.keyDF+'_'+tabNameDataFrame[i] for i in range(0,3)]]
        testIn['hourMod']=toPlot['hourMod']
        testIn[var2.keyDF+'_CoSim']=toPlot[var2.keyDF+'_CoSim']
        testIn=testIn.set_index('hourMod')
             
        testIn.iplot(kind='scatter',                                    title=titleFunc, xTitle='hour (h)', yTitle='$'+var1.lat+'('+var1.unitVar+')$',                                    secondary_y=var2.keyDF+'_CoSim',                                    secondary_y_title='$'+var2.lat+'('+var2.unitVar+')$',showlegend=True)    


# In[62]:


interactive_plot2VarDay = interactive(plot2VarDay, NHour=fixed(96), dayStart=IntSlider(min=0, max=df['hour(h)'].size//24-4, step=1, value=170),                                ControlModel=[(tabNameDataFrame[i],i) for i in range(0,5)],                               var1=[(tabVar[i].varDescription,tabVar[i]) for i in range(1,len(nameColumns))],                             var2=[(tabVar[i].varDescription,tabVar[i]) for i in range(1,len(nameColumns))])
output2VarDay = interactive_plot2VarDay.children[-1]
output2VarDay.layout.height = '450px'
interactive_plot2VarDay


# In[29]:


#plot2VarDay(interactive_plot2VarDay.kwargs['NHour'],interactive_plot2VarDay.kwargs['ControlModel'],interactive_plot2VarDay.kwargs['dayStart'],\
#           interactive_plot2VarDay.kwargs['var1'],interactive_plot2VarDay.kwargs['var2'])


# In[54]:


df[124:248].iplot(y='mdotSF(kg/s)',secondary_y='DNI(W/m2)',x='hour(h)')


# In[ ]:




