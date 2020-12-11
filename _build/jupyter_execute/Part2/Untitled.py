#!/usr/bin/env python
# coding: utf-8

# # Essai de passage de a1, a2 pour un flat plate sur l'aire à des coeffs pour l'équa diff en dT/dz

# Plus précisément, on a en général la définition: $\dot{m} \times C_p \times (T_{out}-T_{in}) = \eta_0 \times A \times I - a_1 * A* (\bar{T}-T_{amb}) - a_2*A*(\bar{T}-T_{amb})^2 $
# 
# $a_1$ et $a_2$ sont fournis par le constructeur de manière classique. Néanmoins, l'équation bilan sur un élément dz du panneau donne:
# 
# $\dot{m} \times C_p \times \frac{dT}{dz} = \eta_0 \times l \times I -\alpha_1 \times l \times (T(z)-T_{amb})-\alpha_2 \times l \times (T(z)-T_{amb})^2$
# 
# Etant donné que cette dernière formulation est plus pratique que la première lorsqu'il s'agit d'étudier un champ solaire constitué de plusieurs panneaux à la suite (en supposant qu'il n'y a pas de pertes dans les connections..), il serait bien de pouvoir passer de l'un à l'autre. Instinctivement, on voudrait les relier par $ \alpha_1 = \frac{a_1}{L} $ avec L la longueur du panneau. Comment vérifier cela? 
# 
# Il est possible de résoudre de manière analytique la deuxième équation, en passant par un argth. En effet, si l'on suppose que la température ne fait que grimper dans le panneau (et donc que $\frac{dT}{dz}>0$), il est possible d'arriver sur l'équation différentielle suivante: 
# $$
# \frac{dT^*}{1-T^{*2}} = \nu_2 \times \sqrt{\frac{A}{\nu_2}+\frac{\nu_1^2}{4 \times \nu_2^2}} \\
# avec \ T^* = \frac{T-T_{amb}+\frac{\nu_1}{2 \times \nu_2}}{\sqrt{\frac{A}{\nu_2}+\frac{\nu_1^2}{4 \times \nu_2^2}}} , \\
#  A = \frac{\eta_0 \times l \times I}{\dot{m} \times C_p}, \\
#  \nu_1 = \frac{\alpha_1}{\dot{m} \times C_p}, \\
#  \nu_2 = \frac{\alpha_2}{\dot{m} \times C_p}
# $$
# 

# $\frac{dT}{dz}>0$ implique que $T^*<1$, et donc que la solution de cette équation différentielle est bien un argth. Cela donne:
# $$
# d \ argth(T^*) = \nu_2 \times \sqrt{\frac{A}{\nu_2}+\frac{\nu_1^2}{4 \times \nu_2^2}} = M, \\
# donc: \ T^* = th(argth(T^*(0))+M*z) = \frac{T^*(0)+th (z \times M)}{1+T^*(0) \times th(z \times M)}
# $$

# L'objectif va donc être de trouver $\alpha_1 , \alpha_2$ tels que les pertes linéaires et les pertes quadratiques s'égalisent. Cela est complexe analytiquement, car nous avons un grand nombre de fonctions non linéaires intervenant dans l'égalité. Nous allons donc tracer la fonction en faisant varier les divers paramètres et voir si la solution instinctive est juste (càd, si T est linéaire dans le panneau).

# Au final, pareil pour le panneau ou tout autre chose: c'est linéaire SI le mdot est assez gros, that is the question. On va donc tracer T(L) en fonction de mdot.
#     

# In[3]:


import math
eta0=0.831
a1 = 3.08
a2 = 0.01
Cp=4187
l=1
Tamb=10


# In[23]:


class Panneau:
    def __init__(self, Tin, eta0, a1, a2, I, Tamb, mdot, Cp, Ap):
        self.Tin=Tin
        a= a2*Ap/4
        b= mdot*Cp+a1*Ap/2-a2*Ap*(Tin/2-Tamb)
        c=eta0*Ap*I+a1*(Tamb-Tin/2)*Ap-a2*Ap*(Tin/2-Tamb)+mdot*Cp*Tin
        c=-c
        delta=b*b-4*a*c
        self.Tout = (-b+math.sqrt(delta))/(2*a)


# In[24]:


Nb=12
T0=Tamb
I=750
mdot=20*12/3600
tabPan=[Panneau(T0,eta0,a1,a2,I,Tamb, mdot, 4187, 2)]
for pan in range(0,Nb):
    tabPan.append(Panneau(tabPan[-1].Tout,eta0,a1,a2,I,Tamb, mdot, 4187, 2))


# In[25]:


for k in range(0,Nb):
    print(tabPan[k].Tin, '-->',tabPan[k].Tout)


# In[26]:


for k in range(0,Nb):
    print((tabPan[k].Tout-tabPan[k].Tin)*mdot*Cp/(2*I))


# In[31]:


eta0 - a1*(54-Tamb)/I - a2*(54-Tamb)*(54-Tamb)/I 


# In[ ]:




