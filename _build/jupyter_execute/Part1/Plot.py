#!/usr/bin/env python
# coding: utf-8

# # Plotter 

# Nous allons ici plotter via plotly et cufflinks, qui permettent une visualisation rapide et efficace d'un certain nombre de données.
# 
# Il est nécessaire de se renseigner sur pandas et les DataFrame pour obtenir les fonctions de manipulation les plus pratiques.
# 
# La méthode implémentée ici est de créer un DataFrame , puis d'appeler dessus la méthode .iplot() (implémentée dans cufflinks). Une autre méthode est d'utiliser directement plotly en rajoutant différents layout sur une figure.
# 
# Il y a un certain nombre d'options dans iplot(); par exemple:
# * y = ['mdot(h)'] -> choisit la fonction en y, possibilité de mettre plusieurs clés
# * secondary_y -> pareil mais pour le deuxième axe
# * kind = 'box' -> type de graphiques. Une courbe simple: 'scatter'; beaucoup de styles sont implémentés
# 
# De nombreux paramètres sont accessibles via help(cf.iplot)

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


# **Exo 1** : Pour n entier naturel non nul, on pose $H_n = \sum_{k=1}^n \frac{1}{k} $  (série harmonique).
# 1) Montrer que : $\forall n \in \mathbb{N}, \ln(n + 1) < H_n < 1 + \ln(n)$ et en déduire la limite en $+\infty$ de $H_n$.
# 
# 2) Pour n entier naturel non nul, on pose $u_n = H_n − ln(n)$ et $v_n = H_n − ln(n + 1)$. Montrer que les suites $(u_n)$ et $(v_n)$ convergent vers un réel γ.

# In[2]:


from math import log
nMax=100
logN=[1+log(n) for n in range(1,nMax+1)]
logNPlus1=[log(n+1) for n in range(1,nMax+1)]

Hn=[1./1.]

for k in range(2,nMax+1):
    Hn.append(Hn[-1]+1./k)
#Pour créer le DataFrame, il faut lui donner une matrice de la bonne taille
data=[Hn,logN,logNPlus1]
#il faut transposer le dataFrame (pas dans le bon sens)
df=pd.DataFrame(data=data).T
# df.describe() : affiche une description du DataFrame
df.columns=["$H_n$","1+ln(n)","ln(n+1)"]
df.iplot(kind='scatter',title='Différentes suites')


# Il est possible de supprimer des cellules, ceci est un test avant de passer à de l'interactif :D

# In[3]:


import plotly.io as pio
import plotly.express as px
import plotly.offline as py

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", size="sepal_length")
fig


# In[ ]:




