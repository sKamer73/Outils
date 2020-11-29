# Tutoriel pour faire un livre interactif
Outils numériques pour la création de livres (pdf) via des notebook Jupyter. 

### La consultation du rendu se fait en ouvrant _build/html/index.html ou _build/latex/MathBook.pdf

#### Divers logiciels / packages ont été téléchargé, voici un résumé des différents wrappers/bonus à ajouter à conda, étape par étape.
Il est intéressant de se familiariser avec chacune des étapes 

## 1. Utilisation d'un notebook pour plotter via pandas, plotly et cufflinks

Prérequis: Anaconda 3
Entrer dans la console (Anaconda Prompt Shell) les instructions suivantes: conda install ** avec ** les packages suivants:

* cufflinks
* pandas
* plotly
* ipywidgets

Possibilité de créer des .html facilement, .pdf, càd une page du notebook, faire tourner quelques plots pour un export facile, ..

Ouvrir un fichier .ipynb dans le dossier pour un exemple.

Il est bien sur possible d'utiliser de manière plus classique matplotlib, ou tout autre package.

## 2. Utilisation de Jupyter Lab 

Les différences JupyterLab/Notebook: le notebook est plus simple d'utilisation au début, mais a une interface moins pratique une fois qu'on a compris comment marche les notebooks. Entre autre, pour l'édition de livres, il est facile de changer les tags des cellules afin de choisir si elle s'affiche dans le rendu final (.html, .pdf).

Le désavantage: des fois besoin de fouiller un peu plus pour pouvoir faire facilement des exportations, etc. 

Pour utilisation de tout cela dans JupyterLab (mais pas Notebook), il faut rajouter des choses à Jupyter Lab. 
Les packages suivants servent à relier 
* conda install jupyterlab "ipywidgets=7.5"
* conda install nodejs
* jupyter labextension install jupyterlab-plotly@4.13.0
* jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.13.0

Commande à mettre dans la console pour conversion en html, en enlevant les cellules avec tags remove_cell et avec remove_input, en étant dans le bon dossier et en remplaçant Plotting par le nom du notebook:

jupyter nbconvert Plotting.ipynb --to=html --TagRemovePreprocessor.remove_input_tags="{'remove_input','remove_cell'}" --TagRemovePreprocessor.remove_single_output_tags="{'remove_cell'}"

Ceci marche si nbconvert est bien configuré. Leur website aide bien (connexion de latex, etc.). Résoudre cela permet d'exporter au format latex puis pdf des notebooks par la commande ci-dessus, en ayant tagué les cellules dans JupyterLab.

### 2.2 Utilisation de Builder pour le partage de notebook interactifs: 

Les notebooks peuvent être partagés à des gens ne possédant pas l'installation Jupyter, en faisant tourner le notebook sur un serveur. Cela est très "convenient", permettant à des élèves, par exemples, de jouer avec des notebooks. 

Le seul bémol: il est bien plus simple de partager un tel document de manière public, que de manière privée; bien que cela semble faisable.

Blinder fait tourner un serveur sur lequel va tourner une version temporaire du notebook.
Pour faire cela, il est nécessaire d'avoir un fichier "requirements.txt" dans lequel les packages nécessaires pour faire tourner les notebook (i.e., les import dans les notebook) doivent être référencés. 

Ensuite, il suffit d'entrer l'adresse du dossier GitHub sur le site de binder: https://mybinder.org/ pour pouvoir, sans inscription aucune, faire tourner un Jupyter en "lecture seule" dans le dossier GitHub. Il est possible de choisir la version de Jupyter (Notebook ou Lab) à ouvrir.


## 3. Jupyter-Book

Moins développé que les applications ci-dessus qui me semblent assez stable, il est nécessaire de suivre les instructions de leur website: https://jupyterbook.org/start/overview.html

Beaucoup d'options intéressantes: mettre des liens pour Binder, 

Pour contruire le livre, sous Windows: 
ouvrir une invite de commande conda, entrer l'instruction suivante afin d'ouvrir l'environnement windows/conda adapté et décrit dans environment_win.yml

conda env create -f environment_win.yml
conda activate wintest

Une fois l'environnement créé, il suffit de taper conda activate wintest afin de réouvrir, dans une autre console par exemple.

Cela ouvre l'environnement conda et donne un nouvel aspect à la console. Il suffit alors d'entrer la commande:
* jupyter-book build Outils/          -----> pour une version html
* jupyter-book build Outils/ --builder pdflatex         -------> pour une version pdf



