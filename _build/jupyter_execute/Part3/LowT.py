#!/usr/bin/env python
# coding: utf-8

# # Basses Températures

# ## Introduction

# Les panneaux solaires basses températures sont, d'après moi, regroupés en trois catégories, fonction de leur technologie et de la température atteignable en sortie. 
# 
# Il y a aujourd'hui trois technologies "mainstream":
# 1. Des tubes noirs, sans protection, au soleil. Utilisé dans les piscines
# 2. Des collecteurs plans: une vitre protégeant un absorbeur noir, derrière lequel passe un tuyau dans lequel cricule le fluide caloporteur.
# 3. Des tubes sous vides (ETC, evacuated tube collectors): des tubes en verre dans lesquels un absorbeur noir récupère la chaleur. Il y a soit un caloduc, soit une circulation direct du fluide caloporteur. Les tubes étant sous vide, les pertes par convection sont minimisées.
# 
# Le fluide caloporteur est le plus souvent de l'eau. Sous nos latitudes, on mélange l'eau avec du glycol afin d'éviter que cette dernière ne gèle la nuit. Il est donc nécessaire d'installer un échangeur entre le stockage et le panneau solaire.
# 
# L'énergie incidente sur le collecteur est caractérisé par les propriétés optiques du système: le verre laisse passer une certaine portion du rayonnement; de même, l'absorbeur n'absorbe pas tout le rayonnement. 

# ### Pertes thermiques 

# Les transferts thermiques se font de trois manières: rayonnement, conduction et convection. Il est donc intéressant de travailler à réduire les pertes par les trois modes de transfert de la chaleur.
# 
# 1. Conduction: l'arrière des panneaux est isolé.
# 2. Rayonnement: le verre possède un spectre d'absorption des infrarouges lointains, ce qui correspond aux émissions basse température.
# 3. Convection: l'air permet un transfert de chaleur, néanmoins son non-renouvellement permet une montée en température (effet de serre). Sous vide, le transfert est encore plus faible.
# 
# Chacun des termes a une expression classique; les pertes par conduction et convection sont proportionelles à $T-T_{amb}$, celles par rayonnement à $T^4-T_{amb}^4$. Sur une petite plage de calculs, il est possible d'écrire cela $(T^2-T_{amb}^2)*(T^2+T_{amb}^2$ et de considérer le deuxième terme constant. Des normes ont donc été mises en place pour le calcul des pertes thermiques.

# #### Modélisation habituelle

# Les pertes thermiques des collecteurs sont déterminés expérimentalement par les constructeurs. Ces pertes, en Watt par m² de collecteur, s'écrivent:

# $$ 
# P_{pertes} = a_1 \times (\bar{T}-T_{amb})+a_2 \times (\bar{T}-T_{amb})^2 
# $$

# Avec $\bar{T}=\frac{T_{inlet}+T_{outlet}}{2}$ la température moyenne dans le panneau. $a_1$ et $a_2$ sont déterminés expérimentalement. 
# 
# $\bar{T}$: ceci est la moyenne dans le panneau. Définie de manière classique, càd: $\bar{T}=\frac{1}{L} \times \int_0^{L} T(z)dz$, il peut être intéressant de se demander si cette dernière est vraiment égale à la moyenne de la température d'entrée et de sortie. Cela est "très" vraie si la température dans le panneau est linéaire, ce qui est le cas selon la plage de fonctionnement.

# ### Energie utile récupérée -- Calcul de la température de sortie

# L'énergie utile récupérée par le panneau s'écrit:

# $$
# \dot{m} \times C_p \times (T_{outlet}-T_{inlet}) = (P_{in}-P_{pertes}) \times A_{panneau}
# $$

# Avec $\dot{m}$ le débit dans le panneau solaire en kg/s, $C_p$ la capacité calorifique du fluide caloporteur en J/kg.K, $P_{in}$ la puissance en entrée du collecteur en W/m², $P_{pertes}$ les pertes en W/m² du panneau.

# On peut écrire $P_{in } = \eta_{opt} * G$ avec G l'irrdiance incidente en W/m² et $\eta_{opt}$ l'efficacité optique du collecteur. Dans le cadre des capteurs basses températures, il s'agit en général du produit de la transparence du verre par l'absorptivité du récepteur. 

# Nous obtenons donc une relation entre: 
# * la température en entrée du panneau du fluide caloporteur
# * la température en sortie
# * le débit dans le panneau solaire
# * la puissance solaire en entrée

# Selon l'inconnue et les paramètres, nous pouvons en déduire une des variables. Il peut être d'intéressant d'optimiser le débit afin de maximiser l'énergie totale du système. C'est le but de mon doctorat, environ. 

# ### Exercices

# 1. Exprimer la température de sortie en fonction des autres variables.
# 2. Avec les paramètres suivants: $\eta_{opt}=0.8, \ a_1 = 3.01 W/m².K , \ a_2=0.2 W/m².K²$ et en choisissant des valeurs plausibles pour les autres paramètres

# Il faut résoudre l'équation de degré 2. Les résultats sont:

# $$
# T_{out} = 
# $$

# ## Bilan sur le stockage

# De manière très simplifiée (en ignorant la stratification par exemple), on peut définir une température moyenne de stockage.

# Dans une maison française post-nucléarisation, le chauffe-eau est souvent électrique. Certains tarifs d'EDF rémunèrent l'utilisation d'Heures Creuses, afin de lisser la demande électrique sur le réseau. Par conséquent, un nombre certain de chauffe-eau s'allument à 22H, ainsi que d'autres appareils électroménagers comme les machines. Ce qui donne les courbes de demande électrique suivante:

# Une équation bilan serait : $M\times \frac{dh}{dt}= \dot{q}_{in}-\dot{q}_{out}-\dot{q}_{pertes}$, avec *h* l'enthalpie du fluide dans le stockage, M la masse du stockage, $\dot{q}_{in}=\dot{m} \times C_p \times (T_{out,panneau}-T_{stockage})$ ,  $\dot{q}_{out}=\dot{m}_{demande} \times C_p \times (T_{stockage}-T_{reseau})$ et $\dot{q}_{pertes}= UA \times (T_{stockage}-T_{ambient})$. $dh = C_p \times dT$

# On obtient donc une équation différentielle en z. Il va donc falloir la résoudre. Cela est fait de manière très classique en discrétisant le temps, par exemple au niveau horaire, ce que l'on fait en prenant $\delta t = 3600s$ et en remplaçant $\frac{dT(t)}{dt} = \frac{T_{n+1}-T_n}{\delta t}$. $T_n$ correspond à la température à l'heure n. On obtient alors la température à l'heure n+1 via l'équation bilan. De proche en proche, cela permet de résoudre la température dans le panneau.

# ### Exercice

# Calculer la température du stockage au cours d'une journée avec l'irradiance définie comme ci-dessous pour le panneau de l'exercice précédent, en utilisant les valeurs de $\dot{m}_{demande}$ présentes dans les photos du livre ainsi que celle de $T_{reseau}$.

# In[17]:


import sympy
import math
sympy.init_printing()
x = sympy.Symbol('x')


# In[24]:


polynomial = 10*x**4+5*x+10
polynomial.expand()


# In[26]:


sols=sympy.solve(polynomial)


# In[31]:


sols[1].evalf()


# In[14]:


x = sympy.Symbol("x")


# In[16]:


sympy.roots(x**2+x+1)


# In[ ]:




