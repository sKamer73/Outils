#!/usr/bin/env python
# coding: utf-8

# # Température de paroi dans une tour

# ## Sur une formule générale

# ### A un instant t donné

# $$
# \dot{m} \times C_p \times \frac{dT}{dz} = \alpha \times \eta_{opt} \times DNI \times \frac{A_{col}}{L_{rec}} - h \times l_{rec} \times (T_p-T_{amb}) - \epsilon (T_p) \times \sigma \times l_{rec} \times (T_p^4-T_{amb}^4)
# $$ (eqGenTFixed)

# La relation entre la température du fluide en z et la température de paroi externe peut être résolue en faisant un bilan sur un élément de la paroi du récepteur:
# $$
# \dot{q}_{SF} (z) = R_{eq}  \times (T_p -T_{fl}(z)) + h_a  \times (T_p-T_{amb} ) + \epsilon \times \sigma  \times (T_p^4-T_{amb}^4) 
# $$

# Avec $\frac{1}{Req} = \frac{e}{\lambda}+\frac{1}{h_{fl}}$

# Ce qui peut s'écrire comme une équation de degré 4 sur $T_p$:
# $$
# T_p^4+ q \times T_p - r =0 \\
#  q= \frac{R_{eq} + h}{\epsilon \times \sigma} \\
#  r = T_{amb}^4 + \frac{\dot{q}_{SF} (z) + R_{eq} \times T + h \times T_{amb} }{\epsilon \times \sigma}
# $$

# Cette équation peut se résoudre de manière littérale en utilisant le fait que les coefficients des carrés et cubes sont nuls. Résultante cubique:
# $$
# R(z) = z^3 +4 \times r \times z - q^2 \\
# \Delta_1 = q^4+ \frac{4}{27} \times (4r)^3
# $$

# Or 
# $$
# z_1 = \sqrt[3]{\frac{q^2-\sqrt{\Delta_1}}{2}} + \sqrt[3]{\frac{q^2+\sqrt{\Delta_1}}{2}} \\
# z_2 = j \times \sqrt[3]{\frac{q^2-\sqrt{\Delta_1}}{2}} + \bar{j} \times \sqrt[3]{\frac{q^2+\sqrt{\Delta_1}}{2}}\\
# z_3 = j^2 \times \sqrt[3]{\frac{q^2-\sqrt{\Delta_1}}{2}} + \bar{j}^2 \times \sqrt[3]{\frac{q^2+\sqrt{\Delta_1}}{2}}\\
# $$

# In[2]:


eps = 0.9
sigma = 5.67 * pow(10,-8)
Tamb=20+273.15
Tsky=273.15
qdotSF=0.9*0.75*1000*800 #alpha*eta_opt*C*DNI
Req= 100*(400/0.1)/(100+4000)
Tfluid=600+273.15
h=10
q=(Req+h)/(eps*sigma)
r=(eps*sigma*pow(Tamb,4)+qdotSF+Req*Tfluid+h*Tamb)/(eps*sigma)
ratio=pow(r,3)/pow(q,4)
nu=4*pow(12,3)/pow(27,2)*ratio
delta0=-12*r
delta1=-27*pow(q,2)
nu2 = -4 *pow(delta0,3)/pow(delta1,2)


# In[120]:


C=pow((1+sqrt(1+nu))/2,1/3)*pow(-delta1,1/3)*(-1)


# In[121]:


C


# In[122]:


import cmath
j=-1/2+1j*sqrt(3)/2
x0=-1/3*(C+delta0/C)
x1=-1/3*(C*j+delta0/(j*C))
x2=-1/3*(C*pow(j,2)+delta0/(pow(j,2)*C))


# In[123]:


sq0=cmath.sqrt(x0)
sq1=cmath.sqrt(x1)
sq2=cmath.sqrt(x2)


# In[124]:


Tp=1/2*(sq0+sq1+sq2)


# In[125]:


1/2*(sq0-sq1-sq2)


# In[38]:


from math import sqrt
sqrt(1+nu)-(1+nu)


# D'où : 
# $$
# C = \sqrt[3]{\Delta_1} \times \nu^{1/6}
# $$
