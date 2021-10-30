# Furniture price prediction 


### Description
Cette application est faite pour prédire le prix de certaines fournitures, en se basant sur des spécifications comme : la taille, la disponibilité en autres couleurs, la catégorie, etc...

Vous pouvez trouver toutes les tâches de prétraitement et les algorithmes de régression dans le fichier **_Furniture price prediction notebook_**. En exécutant ce dernier, vous allez obtenir le modèle (C'est le fichier **_model.pkl_**). 
Le dataset utilisé est sur le fichier **furniture.csv**.


### Setup
Afin d'installer les packages et librairies nécessaires, il faut exécuter la commande suivante dans le répertoire racine du projet après avoir fait un clone au repository :
> `pip install -r requirements.txt`


### Exécution du projet
L'exécution du projet se fait à l'aide de la commande suivante :
> `uvicorn app3:app --reload`

Pour accéder à l'application, il faut consulter l'endpoint suivant dans le navigateur de votre choix :
> `http://127.0.0.1:8000`

### Technologies 
- FastAPI
- Jinja2
- Uvicorn







