#!/usr/bin/env python
# coding: utf-8

# # Explications

# 
# ## 1. Utilisation d'un notebook pour plotter via pandas, plotly et cufflinks
# 
# Prérequis: Anaconda 3
# 
# Entrer dans la console (Anaconda Prompt Shell) les instructions suivantes: conda install ** avec ** les packages suivants:
# 
# * cufflinks
# * pandas
# * plotly
# * ipywidgets
# 
# Possibilité de créer des .html facilement, .pdf, càd une page du notebook, faire tourner quelques plots pour un export facile, ..
# 
# Ouvrir un fichier .ipynb dans le dossier pour un exemple.
# 
# Il est bien sur possible d'utiliser de manière plus classique matplotlib, ou tout autre package.
# 
# ## 2. Utilisation de Jupyter Lab 
# 
# 
# 1. La poire
# 2. La pomme
# 
# 
# Les différences JupyterLab/Notebook: le notebook est plus simple d'utilisation au début, mais a une interface moins pratique une fois qu'on a compris comment marche les notebooks. Entre autre, pour l'édition de livres, il est facile de changer les tags des cellules afin de choisir si elle s'affiche dans le rendu final (.html, .pdf).
# 
# Le désavantage: des fois besoin de fouiller un peu plus pour pouvoir faire facilement des exportations, etc. 
# 
# Pour utilisation de tout cela dans JupyterLab (mais pas Notebook), il faut rajouter des choses à Jupyter Lab. 
# Les packages suivants servent à relier 
# * conda install jupyterlab "ipywidgets=7.5"
# * conda install nodejs
# * jupyter labextension install jupyterlab-plotly@4.13.0
# * jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.13.0
# 
# Commande à mettre dans la console pour conversion en html, en enlevant les cellules avec tags remove_cell et avec remove_input, en étant dans le bon dossier et en remplaçant Plotting par le nom du notebook:
# 
# jupyter nbconvert Plotting.ipynb --to=html --TagRemovePreprocessor.remove_input_tags="{'remove_input','remove_cell'}" --TagRemovePreprocessor.remove_single_output_tags="{'remove_cell'}"
# 
# Ceci marche si nbconvert est bien configuré. Leur website aide bien (connexion de latex, etc.). Résoudre cela permet d'exporter au format latex puis pdf des notebooks par la commande ci-dessus, en ayant tagué les cellules dans JupyterLab.

# Le jfidkp^qfos

# $X_i=10$

# In[65]:


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


# In[66]:


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


# In[78]:


def calcParam(dfD):
    qBoil=dfD['qBoiler(MWh/day)'].sum()
    qDemandYear=dfD['mdotDemand(kg/s/day)'][0]*1200*(350-50)/pow(10,6)*365
    fSolar=1-qBoil/(qDemandYear)
    savedgas=fSolar*qDemandYear
    return [qBoil/1000,fSolar,savedgas/1000]
textXColumn = ['Boiler Heat (GWh/year)', "solar Fraction", "Saved Gas (GWh/year)"]
dfTest=pd.DataFrame(data=[textXColumn, calcParam(dfDaily), calcParam(dfSM1Daily),calcParam(dfSM2Daily), calcParam(dfMILPDaily)]).T
dfTest.columns=['X', 'CoSim','SM1','SM2', 'MILP']


# In[79]:


fig = go.Figure(data=[go.Table(
    header=dict(values=list(dfTest.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=dfTest.transpose().values.tolist(),
               fill_color='lavender',
               align='left'))
])

fig.show()


# In[73]:


import plotly.io as pio
pio.renderers.default = 'jupyterlab'


# In[ ]:




