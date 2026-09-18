# Démo 1 : premiers pas en science des données

Cette démo présente les environnements Python, Git, NumPy et pandas, puis un premier exemple d’apprentissage automatique.

## Commencer

Suivez la [configuration commune du dépôt](../README.md). Depuis `ift3700-6758`, exécutez `uv sync`, puis ouvrez un notebook avec le noyau **`ift3700-6758/.venv`**. Il n’y a pas d’environnement à créer dans `demo_1`.

## Contenu et ordre conseillé

Les notebooks sont disponibles en [français](notebooks/fr/) et en [anglais](notebooks/en/). Choisissez une langue et suivez cet ordre :

| Notebook | Contenu |
|---|---|
| `00_setup_git_python.ipynb` | Fonctionnement des notebooks, Git et bases de Python |
| `01_numpy.ipynb` | Tableaux, indexation, dimensions et calculs numériques |
| `02_pandas.ipynb` | Exploration, sélection, résumés et graphiques à partir de tables |
| `03_ml_bridge.ipynb` | Variables, séparation entraînement/validation et comparaison d’un modèle à une référence |

Exécutez les cellules dans l’ordre et complétez les exercices au fur et à mesure.

Le [diaporama en français](intro_data_science_demo_fr.pptx) accompagne la séance. Sa première partie illustre l’atelier de configuration ci-dessous; pour travailler dans ce dépôt, utilisez l’environnement commun décrit dans le README racine.

## Atelier facultatif : créer un environnement à la main

Le dossier [`python/`](python/) contient un guide en [français](python/README_fr.md) et en [anglais](python/README.md), ainsi que les scripts de vérification et de remise à zéro.

Cet atelier sert à comprendre la création d’un environnement avec `venv` et pip, sa suppression, puis sa reconstruction avec uv. Faites-le dans une **copie de `demo_1` située hors du dépôt**. Les scripts de cet atelier visent la `.venv` de cette copie, pas l’environnement partagé du cours.

<sub>made by Jaydan Aladro</sub>
