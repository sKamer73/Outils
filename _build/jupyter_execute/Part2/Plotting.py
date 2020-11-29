#!/usr/bin/env python
# coding: utf-8

# # Plot of MILP Solutions

# Ce qu'il manque:
# 1) Modèle du Boiler -> pas efficace en dessous de 50%??
# 
# 2) Recirculation <=> i=Ndiscr -> température? Inertie?
# 
# 3) température de procédé variable

# Voir avec modèle de FriendShip et Condat, comment emplacement boiler géré -> discuter avec Raph, Christian et Valéry sur comment sont gérés les cas de base; Christian = Condat, distinct

# Liste de questions et de besoin, et voir quelles sont les réponses, questions au partenaires industriels possible

# **Biblio sur utilisation du boiler**

# 1) check avec différents projets
# 
# 2) analyse résultats
# 
# 3) Américains

# Coût échangeur et pompe peuvent être + pénalisants que pertes thermiques, est-ce + cher?

# ### Pour utilisation dans JupyterLab

# ---> Anaconda (logiciel)
# 
# Entrer dans la console les instructions suivantes:
# conda install ** with ** the following packages:
# * cufflinks
# * pandas
# * plotly
# * ipywidgets
# 
# Pour utilisation de tout cela dans JupyterLab (mais pas Notebook), il faut rajouter des choses à Jupyter Lab. Entrer dans la console les instructions suivantes:
# * conda install jupyterlab "ipywidgets=7.5"
# * conda install nodejs
# * jupyter labextension install jupyterlab-plotly@4.13.0
# * jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.13.0
# 
# Pour avoir l'auto-complétion, il faut changer le fichier de paramètre ipython-default.py 
# 
# Commande à mettre dans la console pour conversion en html, en enlevant les cellules avec tags remove_cell et avec remove_input, en étant dans le bon dossier et en remplaçant Plotting par le nom du notebook:
# 
# jupyter nbconvert Plotting.ipynb --to=html --TagRemovePreprocessor.remove_input_tags="{'remove_input','remove_cell'}" --TagRemovePreprocessor.remove_single_output_tags="{'remove_cell'}"

# ##### Import packages

# In[1]:


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


# #### Class and variables useful for interactivity

# In[2]:


class nameAndUnit: #only contains the name and the unit, not the value 
    def __init__(self, keyIn, nameVarIn, varDescr='', unitVarIn = '', latIn = '' ):
        self.keyDF=keyIn; #key of the variable in the data Frame
        if unitVarIn=='': # if no parameters for unit, might result in problems if nameVarIn is not in the shape mdot(kg/s)
            interm=nameVarIn.split('(')
            self.nameVar=interm[0]
            self.unitVar=interm[1].split(')')[0]
        else:
            self.nameVar=nameVarIn; #Name of the variable
            self.unitVar= unitVarIn; #Unit of the variable 
        if varDescr=='':
            self.varDescription=nameVarIn; #description of the variable, default : name of the variable
        else:
            self.varDescription = varDescr;
        if latIn=='':
            self.lat=self.nameVar; #Latex representation of variable without dollars
        else:
            self.lat=latIn;


# In[3]:


def fromNumDayToDate(numDay): #gives the date from the number of the day in the year, strating with 0 -> 01/01
    listMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    choiceMonth=0;
    sumDayMonth=0;
    while(sumDayMonth<numDay):
        sumDayMonth+=listMonth[choiceMonth]
        choiceMonth+=1
    if(sumDayMonth==numDay):
        if choiceMonth < 9:
            interm = ('0'+str(choiceMonth+1));
        else:
            interm = str(choiceMonth+1)
        rez='01/'+interm;
    else:
        choiceMonth-=1;
        sumDayMonth-=listMonth[choiceMonth];
        numDayMonth=numDay-sumDayMonth+1;
        if choiceMonth < 9:
            interm = ('0'+str(choiceMonth+1));
        else:
            interm = str(choiceMonth+1)
        if numDayMonth<=9:
            interm2 = '0'+str(numDayMonth)
        else:
            interm2=str(numDayMonth)
        rez = interm2+'/'+interm;
    return rez


# In[4]:


listLat=['\Delta t','DNI', 'T_{amb}', '\dot{m}_{Demand}', 'T_{demand}', '\dot{m}_{SF}', 'T_{SF}', '\dot{m}_{aux}',
    '\dot{q}_{boiler}', '\dot{q}_{abs}','M_{storage}', 'T_{storage}', '\dot{m}_{Storage -> boiler}', '\dot{m}_{SF->Boiler}', '\dot{m}_{SF->Storage}']
varDescription=['Hour','Direct Normal Irradiance', 'Ambient Temperature', 'Demand Mass Flow Rate', 'Temperature Demand', 
                'Mass flow rate from the Solar Field', 'Temperature of the Solar Field', 'Auxiliar Mass flow rate', 
               'Heat From The Boiler', 'Heat absorbed by the receiver','Mass in the Storage', 'Temperature of the storage', 'Mass flow rate from the Storage to the Boiler',
               'Mass flow rate from the Solar Field to the Boiler', 'Mass flow rate from the Solar Field to the Storage']
df = pd.read_csv('CoSim.csv') #read a specific csv file
dfMILP= pd.read_csv('MILP.csv') #read another specific csv file with same fields
dfSM1= pd.read_csv('SM1.csv') #read another specific csv file with same fields
dfSM2= pd.read_csv('SM2.csv') #read another specific csv file with same fields
tabDataFrames=[df,dfSM1,dfSM2, dfMILP]
tabNameDataFrame=['CoSim','SM1','SM2','MILP','3 CoSim']
nameColumns=list(df.columns)
tabVar=[nameAndUnit(nameColumns[i],nameColumns[i],varDescription[i],'',listLat[i]) for i in range(0,len(nameColumns))]


# ## Daily plotting

# 1 variable plot on choice, 4 days range

# In[28]:


def plot1VarDay(NHour, ControlModel, dayStart, var1):
    titleFunc= var1.varDescription + ' in ' + var1.unitVar + ' starting on ' + fromNumDayToDate(dayStart)
    if(ControlModel<4):
        toPlot=tabDataFrames[ControlModel][dayStart*24:dayStart*24+NHour]
        toPlot['hourMod']=(toPlot['hour(h)']-dayStart*24)%NHour
        toPlot=toPlot.set_index('hourMod')
        toPlot.iplot(kind='scatter',y=var1.keyDF , title=titleFunc, xTitle='hour (h)', 
                     yTitle='$'+var1.lat+'('+var1.unitVar+')$',showlegend=True)
    else:
        toPlot=pd.concat([tabDataFrames[i].add_suffix('_'+tabNameDataFrame[i]) for i in range(0,3)], axis=1)[dayStart*24:dayStart*24+NHour]
        toPlot['hourMod']=(toPlot['hour(h)_CoSim']-dayStart*24)%NHour
        toPlot=toPlot.set_index('hourMod')
        toPlot[[var1.keyDF+'_'+tabNameDataFrame[i] for i in range(0,3)]].iplot(kind='scatter',
                                    title=titleFunc, xTitle='hour (h)', yTitle='$'+var1.lat+'('+var1.unitVar+')$',showlegend=True)


# In[29]:


interactive_plot1VarDay = interactive(plot1VarDay, NHour=fixed(96),
                                      ControlModel=[(tabNameDataFrame[i],i) for i in range(0,5)],
                                      dayStart=IntSlider(min=0, max=df['hour(h)'].size//24-4, step=1, value=170),
                                      var1=[(tabVar[i].varDescription,tabVar[i]) for i in range(1,len(nameColumns))]);
output1VarDay = interactive_plot1VarDay.children[-1]
output1VarDay.layout.height = '450px'
interactive_plot1VarDay


# In[153]:


plot1VarDay(interactive_plot1VarDay.kwargs['NHour'],interactive_plot1VarDay.kwargs['ControlModel'],interactive_plot1VarDay.kwargs['dayStart'],           interactive_plot1VarDay.kwargs['var1'])


# ##### Plot 2 variables on choice, 4 days range; 1 for the 3 models, the other for the coSim Models

# In[31]:


def plot2VarDay(NHour, ControlModel, dayStart, var1,var2):
    titleFunc= var1.varDescription + ' & ' + var2.varDescription + ' starting on ' + fromNumDayToDate(dayStart)
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


# In[32]:


interactive_plot2VarDay = interactive(plot2VarDay, NHour=fixed(96), dayStart=IntSlider(min=0, max=df['hour(h)'].size//24-4, step=1, value=170),                                ControlModel=[(tabNameDataFrame[i],i) for i in range(0,5)],                               var1=[(tabVar[i].varDescription,tabVar[i]) for i in range(1,len(nameColumns))],                              var2=[(tabVar[i].varDescription,tabVar[i]) for i in range(1,len(nameColumns))])
output2VarDay = interactive_plot2VarDay.children[-1]
output2VarDay.layout.height = '450px'
interactive_plot2VarDay


# In[154]:


plot2VarDay(interactive_plot2VarDay.kwargs['NHour'],interactive_plot2VarDay.kwargs['ControlModel'],interactive_plot2VarDay.kwargs['dayStart'],           interactive_plot2VarDay.kwargs['var1'],interactive_plot2VarDay.kwargs['var2'])


# ## Yearly Plotting

# #### Yearly Results & parameters

# In[74]:


dfDaily = pd.read_csv('CoSimDaily.csv') #read a specific csv file
dfMILPDaily= pd.read_csv('MILPDaily.csv') #read another specific csv file with same fields
dfSM1Daily= pd.read_csv('SM1Daily.csv') #read another specific csv file with same fields
dfSM2Daily= pd.read_csv('SM2Daily.csv') #read another specific csv file with same fields
tabDaily=[dfDaily, dfSM1Daily, dfSM2Daily, dfMILPDaily]
nameColumnsDay=list(dfDaily.columns)
tabVarDay=[nameAndUnit(nameColumnsDay[i],nameColumnsDay[i],varDescription[i],'',listLat[i]) for i in range(0,len(nameColumnsDay))]


# In[137]:


def calcParam(dfD):
    qBoil=dfD['qBoiler(MWh/day)'].sum()
    qDemandYear=dfD['mdotDemand(kg/s/day)'][0]*1200*(350-50)/pow(10,6)*365
    fSolar=1-qBoil/(qDemandYear)
    savedgas=fSolar*qDemandYear
    return [qBoil/1000,fSolar,savedgas/1000]
fig = go.Figure(data=[go.Table(header=dict(values=['X', 'CoSim','SM1','SM2', 'MILP']),
                 cells=dict(values=[['$\dot{q}_{boiler} (GWh_{year})$', "$f_{solar}$", "$savedGas (GWh_{year})$"], 
                                    calcParam(dfDaily), calcParam(dfSM1Daily),calcParam(dfSM2Daily), calcParam(dfMILPDaily)]))
                     ])
fig.layout.height=100
fig.show();


# ### Plot of average values

# In[79]:


def plot1VarYear(ControlModel, var1):
    titleFunc= var1.varDescription + ' in ' + var1.unitVar
    if(ControlModel<4):
        toPlot=tabDaily[ControlModel]
        toPlot['date']=toPlot['day(d)'].map(fromNumDayToDate)
        toPlot=toPlot.set_index('date')
        toPlot.iplot(mode='markers',y=var1.keyDF , title=titleFunc, xTitle='day (d)', symbol='square', size=4,
                     yTitle='$'+var1.lat+'('+var1.unitVar+')$',showlegend=True)
    else:
        toPlot=pd.concat([tabDaily[i].add_suffix('_'+tabNameDataFrame[i]) for i in range(0,3)], axis=1)
        toPlot['date']=toPlot['day(d)_CoSim'].map(fromNumDayToDate)
        toPlot=toPlot.set_index('date')
        toPlot[[var1.keyDF+'_'+tabNameDataFrame[i] for i in range(0,3)]].iplot(mode='markers', symbol='square', size=4,
                                    title=titleFunc, xTitle='day (d)', yTitle='$'+var1.lat+'('+var1.unitVar+')$',showlegend=True)


# In[80]:


interactive_plot1VarYear = interactive(plot1VarYear,
                                      ControlModel=[(tabNameDataFrame[i],i) for i in range(0,5)],
                                      var1=[(tabVarDay[i].varDescription,tabVarDay[i]) for i in range(1,len(nameColumnsDay))]);
output1VarYear = interactive_plot1VarYear.children[-1]
output1VarYear.layout.height = '450px'
interactive_plot1VarYear


# In[129]:


plot1VarYear(interactive_plot1VarYear.kwargs['ControlModel'],interactive_plot1VarYear.kwargs['var1'])


# #### HeatMaps

# In[151]:


def heatMapFromVarName(var, ControlModel):
    df=tabDataFrames[ControlModel]
    nbDays= df[var.keyDF].size//24;
    data=[[df[var.keyDF][day*24+hour] for hour in range(0,24)]  for day in range(0,nbDays)];
    titleFunc = 'Heatmap of the '+var.varDescription +' in '+var.unitVar+' through the year';
    test10=pd.DataFrame(data,index = [fromNumDayToDate(k) for k in range(0,nbDays)]);
    test10.iplot(kind='heatmap', title = titleFunc, colorscale ='spectral',                  showlegend=True, text=var.keyDF );


# In[152]:


interactive_plotHM = interactive(heatMapFromVarName, var=[(tabVar[i].varDescription,tabVar[i]) for i in range(1,len(nameColumns))],
                              ControlModel=[(tabNameDataFrame[i],i) for i in range(0,4)])
outputHM = interactive_plotHM.children[-1]
outputHM.layout.height = '450px'
interactive_plotHM


# In[155]:


heatMapFromVarName(interactive_plotHM.kwargs['var'],interactive_plotHM.kwargs['ControlModel']);


# In[89]:


df.corr().iplot(kind='heatmap',colorscale="Blues", title="Correlation between variables along the year",  showlegend=True)


# In[139]:


def plotRepart(var):
    toPlot=pd.concat([tabDaily[i][var.keyDF] for i in range(0,4)], axis=1)
    toPlot.columns=tabNameDataFrame[0:-1]
    toPlot.iplot(kind='box',xTitle="Control Model", yTitle = var.unitVar,
                 title=var.varDescription + ' average repartition trough the year of daily values', showlegend=False)


# In[140]:


interactive_plotBox = interactive(plotRepart, var=[(tabVarDay[i].varDescription,tabVarDay[i]) for i in range(1,len(nameColumns))])
outputHM = interactive_plotBox.children[-1]
outputHM.layout.height = '450px'
interactive_plotBox


# In[130]:


plotRepart(interactive_plotBox.kwargs['var']);


# In[ ]:




