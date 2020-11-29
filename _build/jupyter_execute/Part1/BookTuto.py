#!/usr/bin/env python
# coding: utf-8

# # Faire un livre avec Jupyter Book

# Je compte présenter ici ma manière de faire, pas donner un cours: c'est encore brouillon dans ma tête.

# Leur website est très bien fait: https://jupyterbook.org/start/overview.html
# 
# Le concept est de créer un livre de notebooks, en générant chaque page et en les ajoutant les uns avec les autres. Cela correspond à une architecture de dossiers/fichiers. Certaines choses peuvent se révéler compliqués lorsque l'on exporte au format pdf, particulièrement au niveau des figures. Le fichier _toc.yml référence l'architecture.
# 
# Il y a beaucoup d'options intéressantes: mettre des liens pour Binder, pour Github, qui permettent un accès rapide à l'interactivité des Notebook
# 
# Pour contruire le livre, sous Windows: 
# ouvrir une invite de commande conda, entrer l'instruction suivante afin d'ouvrir l'environnement windows/conda adapté et décrit dans environment_win.yml
# 
# conda env create -f environment_win.yml
# 
# conda activate wintest
# 
# Une fois l'environnement créé, il suffit de taper conda activate wintest afin de réouvrir, dans une autre console par exemple.
# 
# Cela ouvre l'environnement conda et donne un nouvel aspect à la console. Il suffit alors d'entrer la commande:
# * jupyter-book build Outils/          -----> pour une version html
# * jupyter-book build Outils/ --builder pdflatex         -------> pour une version pdf
