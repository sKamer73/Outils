#!/usr/bin/env python
# coding: utf-8

# # Faire un livre avec Jupyter Book

# ## Motivations

# La simplicité de ce système de **Jupyter Book** est particulièrement pertinente. Le Book est en fait un assemblement des Notebooks, et une façon de les organiser; chaque Notebook est une page, ou plus précisément une partie/chapitre. Organisés de la bonne manière, ils permettent la création d'un site web tel que celui que vous consultez actuellement. De plus, il est facile de faire tourner des codes en arrière plan; par conséquent, cela est très pratique pour toute présentation, dans laquelle on pourrait vous demander de faire quelques calculs légers. De même, faire un site web à partir de vos éléments de présentation devient assez simple, ce qui permet de tout simplement envoyer des liens contenant votre présentation. 

# **Un tutoriel en anglais très bien fait**: https://jupyterbook.org/start/overview.html
# Ce sont eux qui ont créé ce système.

# ## Organisation des notebooks

# ### Dans le dossier

# ![CaptureJupyterArchitecture](../images/CaptureJupyterArchitecture.png)

# Vous pouvez explorer le dossier Github contenant ce livre, en cliquant sur le bouton GitHub en haut à droite. L'architecture (choisie en partie par moi) est la suivante:
# - les dossiers Part1, Part2, .. correspondent aux différentes parties de ce livre (tête de chapitre en gras dans le menu à gauche)
# - les images que je souhaite afficher sont stockés dans le dossier images. 
# - le fichier _config.yml contient la configuration, dans laquelle un certain nombre sont modifiables; voir la [documentation](https://jupyterbook.org/intro.html).
# - le fichier _toc.yml contient l'emplacement de mes notebooks, et l'ordre dans lequel il faut qu'ils apparaissent. Il est facilement modifiable en s'inspirant de celui présent. Ne pas se tromper d'un espace!
# - le dossier build contient votre build, c'est-à-dire sa version html ou pdf. La compilation en pdf est complexe et je ne l'ai pas encore bien cerné.
# - le README.MD vient de Github, c'est ce qui s'affiche dans la présentation du contenu

# ## Compilation du book

# ### Installation de l'environnement wintest

# Il faut utiliser un environnement spécifique à jupyter book *à l'instant où cela est écrit* et ce **sous Windows** car il y a quelques problèmes de compatibilité so far - et si j'ai bien compris. 
# Pour créer l'environnement:
# 1. ouvrir une invite de commande conda comme Anaconda Powershell Prompt présent dans le dossier Anaconda, menu Démarrer
# 2. se déplacer dans les dossiers jusqu'au dossier de ce livre, en utilisant les commandes Linux cd (et ls)
# 3. entrer la commande suivante ->  *conda env create -f environment_win.yml*

# #### Changer l'environnement

# ![Environnement](../images/CaptureEnvironnement.PNG)

# Changer l'environnement est utile pour utiliser d'autres packages dans le Book. Il suffit de les ajouter dans dependencies (ou dans pip si cela ne fonctionne pas).

# ### Compilation en version html

# Compiler le livre revient à entrer une ligne dans l'invite de commande conda. Dans le cas de Windows, il y en a 2: 
# 1. *conda activate wintest*  -> activation de l'environnement précédent
# 2. jupyter-book build Outils/  -> compilation du livre. Si tout se passe bien, le livre se trouvera dans *_build/html*

# Il suffit alors d'ouvrir une page web (.html), puis de se déplacer dans le livre comme sur ce site web.

# ### Compilation en version pdf

# Le compilateur fait passer du notebook à du latex, puis du latex à un pdf. Il peut donc y avoir un soucis au niveau de l'une des deux compilations, et cela est dur à trouver. Je pense qu'il y aura bientôt de l'évolution sur le sujet.
# Cela est appelé à changer bientôt je pense, il y a l'air d'avoir beaucoup d'activités sur leur GitHub.

# La commande pour construire le livre en pdf, **une fois** l'environnement ouvert, est: *jupyter-book build Outils/ --builder pdflatex*

# ## Publier son livre sur GitHub

# Il est possible de mettre en ligne son site web sur GitHub Pages, qui permet un hébergement gratuit. Pour ceux qui se posent la question, GitHub est aujourd'hui détenu par Microsoft.
# 
# Il est nécessaire:
# 1. De créer un dossier git (il est souvent utile de maîtriser git pour cela.. mais ce n'est pas trop mon cas -- à tenter sur Qwant). Cette page https://jupyterbook.org/start/publish.html explique le nécessaire
# 2. Synchronisation du dossier git via *git commit -m "Message Affichee"* puis *git push*
# 3. Utiliser cette commande *ghp-import -n -p -f _build/html*, qui nécessite que ghp-import soit installé (ce qui se fait via *pip install ghp-import*)

# ## Astuces de présentation spécifiques au book

# Idées: En-tête, margin, 
