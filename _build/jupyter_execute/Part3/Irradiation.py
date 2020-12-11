#!/usr/bin/env python
# coding: utf-8

# # L'irradiation solaire

# Il est possible, d'un point de vue énergétique, de catégoriser l'énergie disponible sur Terre via trois origines: la Terre, le Soleil et la Lune. En effet, du soleil vient:
# - la biomasse (photosynthèse)
# - les énergies fossiles (photosynthèse puis raffinement)
# - le vent (différences de températures, cellules convectives, etc.)
# - l'hydroélectricité (cycle de l'eau, évaporation)
# 
# La Terre donne l'énergie géothermique, càd de l'énergie nucléaire issu de son noyau en fusion. Etant doné que l'uranium est présent sur Terre, on pourrait dire que l'énergie nucléaire par fission est d'origine terrestre. Alors que l'énergie nucléaire par fusion viendrait du big bang?
# 
# La Lune, ainsi que le Soleil, génère des forces de gravité. Ce qui fait bouger les océans, via les marées, d'où l'énergie marémotrice. 
# 
# L'irradiance solaire correspond à la puissance envoyée par le soleil, souvent exprimée en W/m². Le soleil envoie une énergie considérable sur Terre, mais peu dense: en effet, une approximation rapide au niveau du sol donnerait 1000 W/m², pour un beau jour d'été en France. Cette énergie thermique (rayonnement) est récupéré par les différents éléments terrestres puis condensée, stockée, .. Ce qui permet de la récupérer en brûlant du bois, par exemple, ou en stockant l'eau en haut des montagnes. L'énergie hydroéléctrique est bien plus dense que l'énergie solaire: en récupérant l'eau et en la mettant dans un barrage, en grimpant en hauteur, on peut stocker cette énergie.
# 
# L'irradiation solaire correspond à l'énergie arrivant sur une surface; elle est exprimée en Wh/m², c'est par définition l'intégrale au cours du temps de la puissance, càd l'irradiance.

# ## L'absorption et le spectre solaire

# Un corps noir émet une puissance rayonnante, proportionelle à sa température: $\sigma T^4$. $\sigma$ est la constante de Boltzmann, valant $5.67 \times 10^{-8} \ W/K^4$ 

# Plus précisément, un corps noir émet une énergie par longueur d'onde; plus précisément, la formule de Planck nous donne cette répartition par longueur d'onde:
# $$
# \phi_{\lambda} = \frac{2 \pi \times h \times c_0}{\lambda^5} \times \frac{1}{exp(\frac{h \dot c_0}{\lambda k_B T})-1}
# $$

# In[5]:


from math import pi,exp
def Planck(wave,temperature):
    h=6.62*pow(10,-34)
    c0 = 2.99 * pow(10,8)
    kB=1.380649 * pow(10,-23)
    lambd = wave*pow(10,-9) #à donner en nanomètres
    coef1= 2*pi*h*c0/pow(lambd,5)
    coef2= h*c0/(lambd*kB*temperature)
    return coef1/(exp(coef2)-1)


# In[6]:


Planck(500,5900)


# In[ ]:




