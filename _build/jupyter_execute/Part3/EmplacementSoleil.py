#!/usr/bin/env python
# coding: utf-8

# # Décrire l'emplacement du soleil

# Pour décrire l'emplacement du soleil, deux systèmes de coordonnées semblent très pratique: le système de coordonnées **horizontales**, qui pose un repère local; et le système de coordonnées **équatoriales**, qui se place dans un repère héliocentrée.

# ## Azimuth et Elevation - Horizontale

# ```{sidebar} Note
# D'autres bases orthonormées directes sont possibles, comme par exemple Ox orienté à l'ouest et Oy au sud. L'azimuth est alors négatif le matin, entre autres. La définition de l'azimuth est également variable, se méfier.
# ```

# On se place dans un repère (0,x,y,z) orthonormé direct, avec x pointant vers l'est, y vers le nord et z à la verticale. Notons $\vec{s}$ le vecteur solaire, càd un vecteur de norme 1 pointant vers le soleil.
# 
# 
# Comme le soleil se déplace à distance fixe (plus ou moins) de la Terre, il ne se déplace qu'en deux dimensions sur la "sphère céleste. Il est donc possible de décrire sa position avec deux angles,  il est possible de décrire sa position avec 2 angles: l'azimuth et l'élévation. 

# ![dessin](../images/Dessin.PNG)

# Plus d'informations: [Wikipédia](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_coordonn%C3%A9es_horizontales)

# ### Azimuth - $\alpha$

# ![North Azimuth](../images/azimElevCelestial.PNG)

# Cet angle correspond à la direction du soleil dans le plan horizontale; 0° correspond au Nord, 90° à l'est, etc.
# 
# On peut le définir comme l'angle entre
# 1. Le projeté du vecteur solaire $\vec{s}$ dans le plan (0,x,y)
# 2. Le vecteur dirigé au nord ($\vec{Oy}$)

# ### Elevation - $\gamma$

# ![Elevation](../images/elev.PNG)

# L'élevation ($\gamma$) est l'angle formé entre le soleil et la ligne de l'horizon.

# ### Vecteur solaire

# Le vecteur solaire est un vecteur pointant vers le soleil. Sans cette base et pour cette définition de l'azimuth, il s'exprime comme:

# $$
# \vec{s}= \sin(\alpha) \times \cos(\gamma) \vec{u_x} + \cos(\alpha) \times \cos(\gamma) \vec{u_y} + \sin(\gamma) \vec{u_z}
# $$

# In[32]:


class solarVector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def printVec(self):
        print("x--->"+str(self.x)+"\n y--->" +str(self.y)+"\n z---> "+str(self.z))
    def prod(self,vec):
        return (self.x)

def solarVectorFromAzimElev(azim,elev):
    sx = sin(azim) * cos(elev);
    sy = cos(azim) * cos(elev);
    sz = sin(elev);
    return solarVector(sx,sy,sz);
    


# ## Latitude, déclinaison et angle horaire - Systèmes Equatoriales

# Ce repère correspond à un repère héliocentré. Néanmoins, le vecteur solaire est donné dans la base locale d'un observateur situé à la latitude $\phi$ et au temps t. Plus d'informations: [Wikipédia](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_coordonn%C3%A9es_%C3%A9quatoriales)

# ![Déclinaison](../images/declinaison.PNG)

# ### Déclinaison

# La déclinaison ($\delta$) correspond à l'inclinaison de l'axe de la terre. Ce dernier varie de -23.4° au solstice d'hiver à 23.4° au solstice d'été. Cet angle peut être relié au jour de l'année via de nombreuses corrélations, la plus reconnue étant celle de l'algorithme PSA.
# En voici une très proche.

# In[20]:


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


from math import cos, sin
def solarDeclinationByDayNumber(day):
    Pi = 3.14159;
    omega = (2 * Pi) / 365 * (day - 1.);
    return 0.006918 - 0.399912 * cos(omega) - 0.006758 * cos(2 * omega) + 0.000907 * sin(2 * omega) - 0.002697 * cos(3 * omega) + 0.00148 * sin(3 * omega);

xDays=[k for k in range(0,365)]
deltaDays=[solarDeclinationByDayNumber(k) for k in range(0,365)]
dfYear=pd.DataFrame([xDays,deltaDays]).T
dfYear.columns=["day","declination"]
dfYear.iplot(kind='scatter',x="day",y="declination", title="Déclinaison solaire durant l'année", xTitle="day", yTitle=" delta (rad)")


# ### Angle horaire

# L'angle horaire ($\omega$) est défini par la rotation de la Terre par rapport au midi heure solaire. Il vaut 0 à midi, est positif dans l'après-midi et négatif le matin.
# 
# La terre faisant 360° en 24 heures, la Terre décrit $\frac{360 ° }{24h}=15°/h$. Ce qui peut s'écrire $\frac{d \omega}{dt}=15°/h$ avec *t* le temps en heure. D'où, après intégration : $\omega = (t-12)*15 °= \frac{\pi}{180} \times 15 \times (t-12) \ rad $
# 
# Dans cette équation, le temps est en UTC ou heure solaire. En France, (pour l'instant?), l'heure d'été est UTC+2 et hiver UTC+1, c'est-à-dire qu'en hiver le soleil est au sud à 13h et en été à 14h.

# In[22]:


from math import pi
dfDay=pd.DataFrame(data= [[k for k in range(0,24)],[(k-12)*15*pi/180 for k in range(0,24)]]).T
dfDay.columns = ["hour","omega"]
dfDay.iplot(x='hour',y='omega', title = "Angle horaire sur 24 h", xTitle="hour", yTitle="Omega (rad)")


# L'heure maximale $\omega_{max}$, càd l'heure à laquelle le soleil se couche, s'écrit $\omega_{max} = \arccos(-\tan(\phi) \times \tan(\delta) )$

# In[23]:


from math import acos, tan, pi
def omegaMax(day,lat):
    return acos(-tan(lat)*tan(solarDeclinationByDayNumber(day)))


# In[24]:


phi=45.564601 * 3.14159/180;
dfYear['omega_max']=[omegaMax(k,phi) for k in range(0,365)]
dfYear['derivHourMax']=[(omegaMax(k+1,phi)-omegaMax(k,phi))*180/(3.14159*15)*60 for k in range(0,365)]
dfYear['hourMax']=[12+dfYear['omega_max'][k]*180/(3.14159*15) for k in range(0,365)]
dfYear.iplot(x="day",y="hourMax",secondary_y="derivHourMax",
             title="Heure de coucher du soleil et sa dérivée au cours de l'année",
            xTitle="day", yTitle="Heure de coucher (h)", secondary_y_title="Dérivée (minutes/day)")


# ### Vecteur solaire

# Idée de démonstrations: produit de matrices de rotation pour arriver sur le bon repère: Base 0 -> Géocentrée, avec un axe vers le soleil et un z sur la moyenne de l'axe terrestre

# Le vecteur solaire dans la base locale à l'observateur s'écrit alors:

# $$
# \vec{s} = - \cos(\delta) \times \sin(\omega) \vec{u_x}\\
# + (\sin(\delta) \times \cos(\phi) - \cos(\delta) \times \cos(\omega) \times \sin(\phi) ) \times \vec{u_y}\\
# + (\sin(\delta) \times \sin(\phi) + \cos(\delta) \times \cos(\omega) \times \cos(\phi) ) \times \vec{u_z}
# $$

# In[25]:


def solarVectorFromDeclinHour(declination,hourAngle,lat):
    sx = -cos(declination) * sin(hourAngle);
    sy = sin(declination) * cos(lat) - cos(declination) * sin(lat) * cos(hourAngle);
    sz = sin(declination) * sin(lat) + cos(declination) * cos(lat) * cos(hourAngle);
    return solarVector(sx,sy,sz)


# ## Passer d'un système de coordonnées à l'autre

# L'idée est de passer d'un système à l'autre via le vecteur solaire. Les deux formules donnant le vecteur solaire dans le même repère, il devient facile de les inverser. Les algorithmes suivant ont été vérifiés mais on n'est jamais ampte de se planter..

# ### Du vecteur solaire à l'azimuth et l'élévation

# In[26]:


from math import asin, cos, pi
def azimElevFromSolarVector(s):
    elev = asin(s.z);
    interm = asin(s.x / cos(elev)-0.00000000000002);
    if (s.y>0):
        if (s.x > 0):
            azim = interm;
        else:
            azim = 2 * pi + interm;
    else:
        azim = pi - interm;
    return (azim,elev)


# ### Du vecteur solaire à la déclinaison et l'angle horaire

# In[27]:


from math import asin, cos, sin, tan
def declinHourFromSolarVector(s,lat):
    declin = asin((s.y + s.z * tan(lat)) / (cos(lat) + sin(lat) * tan(lat)));
    interm = -asin(s.x / cos(declin));
    test = (sin(declin) * cos(lat) - s.y) / (cos(declin) * sin(lat));
    if (abs(cos(interm) - test) < 0.001):
        hour = interm;
    elif (s.x < 0):
        hour = Pi - interm;
    else:
        hour = -Pi - interm;
    return(declin, hour)


# ### D'un système à l'autre

# In[28]:


def azimElevFromDeclinHour(declin,hour,lat):
    s=solarVectorFromDeclinHour(declin,hour,lat)
    return azimElevFromSolarVector(s)


# In[29]:


def declinHourFromAzimElev(azim,elev,lat):
    s=solarVectorFromAzimElev(azim,elev)
    return declinHourFromSolarVector(s,lat)


# ## Tracés annuels

# A l'aide de la déclinaison, de l'heure et de la latitude, il nous est désormais possible de trouver l'azimuth et l'élévation. Ce système de coordonnées locales est le plus utilisé lorsqu'il s'agit de réfléchir à un système solaire.

# ### Azimuth et élévation

# In[30]:


from math import pi
day=173
degree=pi/180;
dfDay=pd.DataFrame(data=[[k for k in range(0,24)],[(k-12)*15*pi/180 for k in range(0,24)]]).T;
declin=solarDeclinationByDayNumber(day);
hourAngleMax=omegaMax(day,phi);
dfDay.columns = ["hour","omega"];
azimElev=[azimElevFromDeclinHour(declin,dfDay['omega'][k],phi) for k in range(0,24)];
dfDay['azimuth']=[azimElev[k][0]/degree for k in range(0,24)];
dfDay['elevation']=[azimElev[k][1]/degree for k in range(0,24)];
dfDay.iplot(kind='scatter',mode='markers',size=10,symbol='x', x="azimuth", y="elevation", 
            title = "Azimuth vs Elevation during a summer day", xTitle= "Azimuth (°)", yTitle="Elevation (°)", text="hour")


# In[31]:


from math import pi
def plotAzimVsElev(day):
    degree=pi/180;
    dfDay=pd.DataFrame(data=[[k for k in range(0,24)],[(k-12)*15*pi/180 for k in range(0,24)]]).T;
    declin=solarDeclinationByDayNumber(day);
    hourAngleMax=omegaMax(day,phi);
    dfDay.columns = ["hour","omega"];
    azimElev=[azimElevFromDeclinHour(declin,dfDay['omega'][k],phi) for k in range(0,24)];
    dfDay['azimuth']=[azimElev[k][0]/degree for k in range(0,24)];
    dfDay['elevation']=[azimElev[k][1]/degree for k in range(0,24)];
    dfDay.head()
    dfDay.iplot(kind='scatter',mode='markers',size=10,symbol='x', x="azimuth", y="elevation", 
            title = "Azimuth vs Elevation on day n° "+str(day), xTitle= "Azimuth (°)", yTitle="Elevation (°)", text="hour")


# Lorsque l'élévation est négative, cela correspond aux heures à laquelle le soleil ne s'est pas encore levé.

# In[18]:


0.712*0.712+0.1*0.1+0.14*0.14


# In[ ]:




