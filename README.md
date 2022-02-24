# OCP7


Programme comportant plusieurs algorithmes visant à maximiser les profits lors de l'achat d'action.

## donnée d'action :

Pour utiliser le programme veuillez placer vos données d'actions à acheter dans le dossier donnees sous la forme de 
fichier csv avec dans l'ordre le nom, le prix (en euros), le profit (en pourcentage) et utiliser la virgule en 
séparateur.

## utilisation

Dans votre terminal placez-vous à la racine du projet puis :

### Créer votre environnement virtuel :


```bash
python3 -m venv env
```

### Activer votre environnement :

linux ou mac :
```bash
source env/bin/activate
```

windows :

```bash
env\\Scripts\\activate.bat
```

### Installer les packages :

```bash
pip install -r requirements.txt
```

### Executer le programme :

```bash
python3 main.py
```

## Fonctionnement

Le programme commence par vous demander de selectionner le fichier comportant les données et de combien d'argent vous 
disposez.

Ensuite il vous demande quel algorithme utiliser. Il y a trois algorithme :
* L'agorithme "brutal" calcul toutes les solutions et leurs bénefice et l'enregistre dans un fichier 
"brutalsolutions.csv". Il sournit donc une réponse juste mais prend du temps.
* L'algorithme de programation dynamique prend moins de temps. Il construit de manière récursive un tableau pour nous 
permettre de déterminer quelle est la meilleur possibilité. La solution est également exact.
* L'algorithme "glouton" prend dans l'ordre les actions rapportant le plus. Il est très rapide mais la solution 
n'est pas forcément la meilleure.

Enfin le programme calcul et affiche la solution selon l'algorithme que vous avez sélectioné.