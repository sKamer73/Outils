# Tutoriel pour faire un livre interactif

Ce tutoriel est en version Béta.

Dans le cadre de mon doctorat, j'ai commencé à utiliser Python pour tracer des courbes. Je me suis donc intéressé à Jupyter, Notebook puis Lab, car l'interface d'un notebook dans le style Mathematica (ou MatLab? Jamais utilisé) m'a toujours semblé très pratique, pour les raisons suivantes:
* exécution immédiate car pas de compilation
* interactivité: changer sa ligne de code et réappuyer sur maj + entrée
* pratique pour présenter, écriture en Latex, courbes, ..

J'ai ensuite découvert d'autres fonctionnalités qui m'ont fait penser que ce système serait très intéressant pour donner des cours. Le plus évident serait des cours de Python, néanmoins il est tout à fait possible d'écrire des livres en pdf ou html. Les versions html correspondent à un site web, comme peut-être là où vous lisez ce tutoriel. Dans la version html, il est possible d'ajouter des boutons interactif envoyant sur GitHub ou sur Binder. Binder est un serveur qui fait tourner vos notebook à partir de votre dossier GitHub: cela donne accès de manière interactive à votre livre/code en **lecture seule.** 

Du code pour tracer des courbes est également disponible, comme exemple de ce qu'il est possible de faire. J'ai personellement choisi de m'orienter vers Plotly et Cufflinks avec l'usage de bouton interactif (changer le jour, les variables explorées, ...). Cela permet de faire une analyse de données facile. Les données présentes sont issus d'une simulation et ne sont pas privées. 

La première partie de ce tutoriel explique comment faire des livres. Cela est principalement un résumé de ce que j'ai compris, et n'est pas exempt d'erreurs. Par ailleurs, ces logiciels sont en grande évolution; de nombreuses personnes travaillent à faire ces interfaces plus maniables, et je pense que ces outils peuvent devenir une norme.

La seconde partie explique comment tracer des courbes et des exemples d'interactivité sont disponibles dans les NoteBooks. 
