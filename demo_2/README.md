# Démo 2 : de l’API NHL à une table pandas

Cette première partie introduit l’objectif **acquisition et nettoyage des données** du milestone 1 du projet. Ca vous accompagne dans l’utilisation de l’API, à partir d’un seul match : Montréal–Caroline, le 21 mai 2026 (`2025030311`) (🥲).

## Commencer

Suivez la [configuration commune](../README.md) : depuis la racine de `ift3700-6758`, lancez `uv sync`, puis choisissez le noyau de la `.venv` commune.

Ouvrez le [notebook guidé](notebooks/en/01_data_acquisition_and_cleaning.ipynb). Il utilise pandas et requests, déclarés dans l’environnement commun. Vous devez connaître un minimum : les cellules Jupyter, les listes et les dictionnaires; aucune expérience des API n’est nécessaire.

## Déroulement

| Partie | Activité |
|---|---|
| A | Comprendre client, serveur, requête GET, URL et réponse JSON |
| B | Télécharger un match, vérifier la réponse et sauvegarder le JSON |
| C | Recharger le fichier et explorer les dictionnaires et listes |
| D | Aplatir les événements avec `pd.json_normalize` et inspecter la table |
| E | Garder les tirs et buts, nommer les colonnes, vérifier les identifiants et valeurs manquantes |
| F | Exporter un CSV et expliquer les étapes du pipeline |

Deux exercices courts incluent des réponses repliées. La fin distingue les étapes réalisées des exigences restantes du projet : plusieurs saisons, noms des joueurs, filet désert et force numérique.

## Avant la séance

Exécutez une fois le notebook avec une connexion Internet, puis redémarrez le noyau et relancez toutes les cellules. Le deuxième passage doit réutiliser le fichier local. Les dossiers `data/raw` et `data/processed` sont créés relativement au répertoire de travail du noyau; le notebook affiche les chemins complets. Ils sont ignorés par Git.

Gardez le JSON téléchargé pour pouvoir le distribuer séparément si l’API est indisponible en classe. Les étudiants peuvent le placer au chemin affiché, puis poursuivre avec la partie C. Aucun fichier de données n’est inclus dans le dépôt.

Lors de la préparation, l’API renvoyait **339 événements**, dont **42 `shot-on-goal` et 8 `goal`**, soit **50 lignes retenues**. Ces nombres servent de repères pour ce match, pas de constantes à imposer à tous les matchs; le fournisseur peut corriger ses données.
