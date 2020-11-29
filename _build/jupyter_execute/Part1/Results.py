#!/usr/bin/env python
# coding: utf-8

# # Résultats et Discussions

# $X_i=10$

# In[10]:


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


# In[11]:


listLat=['\Delta t','DNI', 'T_{amb}', '\dot{m}_{Demand}', 'T_{demand}', '\dot{m}_{SF}', 'T_{SF}', '\dot{m}_{aux}',
    '\dot{q}_{boiler}', '\dot{q}_{abs}','M_{storage}', 'T_{storage}', '\dot{m}_{Storage -> boiler}', '\dot{m}_{SF->Boiler}', '\dot{m}_{SF->Storage}']
varDescription=['Hour','Direct Normal Irradiance', 'Ambient Temperature', 'Demand Mass Flow Rate', 'Temperature Demand', 
                'Mass flow rate from the Solar Field', 'Temperature of the Solar Field', 'Auxiliar Mass flow rate', 
               'Heat From The Boiler', 'Heat absorbed by the receiver','Mass in the Storage', 'Temperature of the storage', 'Mass flow rate from the Storage to the Boiler',
               'Mass flow rate from the Solar Field to the Boiler', 'Mass flow rate from the Solar Field to the Storage']
dfDaily = pd.read_csv('data/CoSimDaily.csv') #read a specific csv file
dfMILPDaily= pd.read_csv('data/MILPDaily.csv') #read another specific csv file with same fields
dfSM1Daily= pd.read_csv('data/SM1Daily.csv') #read another specific csv file with same fields
dfSM2Daily= pd.read_csv('data/SM2Daily.csv') #read another specific csv file with same fields
tabDaily=[dfDaily, dfSM1Daily, dfSM2Daily, dfMILPDaily]
nameColumnsDay=list(dfDaily.columns)
tabVarDay=[hm.nameAndUnit(nameColumnsDay[i],nameColumnsDay[i],varDescription[i],'',listLat[i]) for i in range(0,len(nameColumnsDay))]


# In[61]:


def calcParam(dfD):
    qBoil=dfD['qBoiler(MWh/day)'].sum()
    qDemandYear=dfD['mdotDemand(kg/s/day)'][0]*1200*(350-50)/pow(10,6)*365
    fSolar=1-qBoil/(qDemandYear)
    savedgas=fSolar*qDemandYear
    return [qBoil/1000,fSolar,savedgas/1000]
textXColumn = ['$Q_{Boiler} (GWh_{year})$', "$f_{solar}$", "$Saved \ Gas (GWh_{year})$"]
dfTest=pd.DataFrame(data=[textXColumn, calcParam(dfDaily), calcParam(dfSM1Daily),calcParam(dfSM2Daily), calcParam(dfMILPDaily)]).T
dfTest.columns=['X', 'CoSim','SM1','SM2', 'MILP']
dfTest.plot(kind='table')


# In[62]:


fig = go.Figure(data=[go.Table(
    header=dict(values=list(dfTest.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=dfTest.transpose().values.tolist(),
               fill_color='lavender',
               align='left'))
])

fig.show()


# In[64]:


import chart_studio.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[1, 4, 9, 16],
    name=r'$\alpha_{1c} = 352 \pm 11 \text{ km s}^{-1}$'
)
trace2 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[0.5, 2, 4.5, 8],
    name=r'$\beta_{1c} = 25 \pm 11 \text{ km s}^{-1}$'
)
data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        title=r'$\sqrt{(n_\text{c}(t|{T_\text{early}}))}$'
    ),
    yaxis=dict(
        title=r'$d, r \text{ (solar radius)}$'
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='latex')


# In[ ]:




