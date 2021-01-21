#!/usr/bin/env python
# coding: utf-8

# # Tutoriel Python & Notebook

# Un cours en **français** est présent à l'adresse suivante: https://python.sdv.univ-paris-diderot.fr/
# 
# Le chapitre 18 introduit à l'utilisation des Notebook et de JupyterLab. A mon avis, l'auteur a utilisé Jupyter Book pour écrire son cours.

# L'intérêt des Notebook réside dans les cellules et l'absence de compilation. L'utilisation de Latex dans les markdown permet de faire de beaux documents avec de belles formules.
# 
# De plus, l'ouverture dans un navigateur internet est un vrai plus. Je mets ici un tuto pour une utilisation rapide, si vous connaissez un peu de Python.

# Vous pouvez télécharger ce Notebook via le bouton télécharger > .ipynb situé en haut de cette page.

# ## Etape 1: Installer Anaconda

# Tout est dans le titre, à chercher sur Qwant ou DuckDuckGo.

# ## Etape 2 : Lancer Jupyter

# Ouvrir Anaconda et cliquer sur jupyter. 
# 
# Il est possible de l'ouvrir depuis l'invite de commande (Anaconda Prompt Shell) si vous n'avez pas envie de lancer le launcher d'Anaconda.
# La commande:
# * jupyter-notebook pour le notebook
# * jupyter lab pour Jupyter Lab

# ## Etape 3 : Jouer avec Python et Jupyter

# Les écritures ci-dessous sont en MarkDown, qui est une sorte de traitement de texte avec du Latex, comme expliqué plus bas.

# **Exo 1** : Pour n entier naturel non nul, on pose $H_n = \sum_{k=1}^n \frac{1}{k} $  (série harmonique).
# 1) Montrer que : $\forall n \in \mathbb{N}, \ln(n + 1) < H_n < 1 + \ln(n)$ et en déduire la limite en $+\infty$ de $H_n$.
# 
# 2) Pour n entier naturel non nul, on pose $u_n = H_n − ln(n)$ et $v_n = H_n − ln(n + 1)$. Montrer que les suites $(u_n)$ et $(v_n)$ convergent vers un réel γ.

# In[1]:


# Import pour plotter de manière facile
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


# In[4]:


from math import log
nMax=100
logN=[1+log(n) for n in range(1,nMax+1)]
logNPlus1=[log(n+1) for n in range(1,nMax+1)]

Hn=[1./1.]

for k in range(2,nMax+1):
    Hn.append(Hn[-1]+1./k)
#Pour tracer
data=[Hn,logN,logNPlus1]
#il faut transposer le dataFrame
df=pd.DataFrame(data=data).T
# df.describe()
df.columns=["$H_n$","1+ln(n)","ln(n+1)"]
df.iplot(kind='scatter',title='Différentes suites')


# ## Etape 4: Exporter votre NoteBook au format pdf ou html

# Cela est possible en allant dans le menu > File > Export noteBook as..
# 
# Il est possible de le faire depuis la ligne de commande via *jupyter nbconvert --to html YourNotebook.ipynb*

# ### Discussion: Avis personnel sur Lab vs notebook

# Lab me semble plus pratique que NoteBook, j'ai commencé avec directement. En fait, Lab est un Wrapper autour de Notebook: on peut utiliser tout le Notebook dans Lab. Ce qui fait que c'est plus compliqué, forcément. Mais on a plus d'options, comme ouvrir une console directement dans le notebook, se déplacer plus facilement dans les fichiers, écrire des méta données dans des cellules, ..
# 
# Néanmoins, j'ai pu avoir des soucis lors de l'exportation au format pdf, que j'avais beaucoup moins avec le NoteBook.

# ## Le MarkDown

# Ceci est une sorte de typographie, utilisé dans beaucoup d'autres codes. Latex est résent dans tout ça: une conversion au latex est faite facilement.
# 
# Voici différentes astuces et idées (non exhaustives) pour écrire en MarkDown:
# 1. Ecrire en italique: encadrer le texte à rendre en italique d'une $*$ de chaque côté
# 2. Ecrire en gras: pareil mais avec deux étoiles: $**$
# 3. Afficher une image: $![UselessTexte](chemin/a/image)$. Dans le cadre de l'architecture du book, on peut utiliser ../images/NomImage.png
# 4. Faire un lien cliquable: $[TexteACliquer](lien)$
# 5. Copier-coller une image -- elle est stocké dans un fichier temporaire, donc lors de l'édition d'un livre elle disparait mais pas lors de "l'impression" d'un unique notebook.
# 6. Ecrire des équations: il faut encadrer du Latex par deux symboles $

# ## JupyterLab: utilisation pratique

# ### Se déplacer facilement

# Il est possible de se déplacer au clavier entre les cellules, ce qui est très pratique. Probablement possible avec le notebook aussi.
# 
# Si vous êtes dans une cellule, appuyez sur échap pour passer en mode "commande": vous pourrez alors:
# * vous déplacer via les flèches
# * ajouter une cellule avant votre position avec a (pour avant) et b après votre position (pas de moyen mnémotechnique)
# * copier une cellule avec c et coller avec v (pas de touche ctrl); couper avec x
# * entrer dans une cellule avec enter
# * modifier le type de la cellule: y -> code, m -> markdown
# * supprimer une cellule en tapant dd

# ### Ouvrir une console

# Clic droit sur l'onglet du notebook > new console for notebook.
# 
# Pratique pour ne pas salir son notebook, se déplacer et tester des choses. Je ne l'utilise pas tant que ça car il est possible d'utiliser les commandes linux (pwd, cd) directement dans le notebook (pour ouvrir des fichiers par exemple).
