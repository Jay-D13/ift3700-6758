# Anciens laboratoires

Les supports des années précédentes sont regroupés **par thème**, puis par langue (`fr/` et `en/`). La numérotation historique des labos variait selon les années : elle n’est plus utilisée pour nommer les dossiers.

Pour chaque thème et chaque langue, nous conservons la version la plus récente identifiable dans les fichiers disponibles. Deux variantes restent présentes lorsqu’elles couvrent des sujets différents. Les années proviennent des titres ou des noms des notebooks, pas de la date de copie des fichiers. « Non daté » signifie qu’aucune année d’édition fiable n’a été trouvée.

## Catalogue publié

Seuls NumPy, pandas et le calcul scientifique sont publiés ici pour le moment. Les autres thèmes restent dans l’archive locale.

| Thème | Français | Anglais | Choix retenu |
|---|---|---|---|
| NumPy | [2025](numpy/fr/numpy_2025.ipynb) | [2025](numpy/en/numpy_2025.ipynb) | Versions centrées sur NumPy |
| pandas | [2025](pandas/fr/pandas_2025.ipynb) | [2025](pandas/en/pandas_2025.ipynb) | Remplacent les cours de 2020/2023 |
| Calcul scientifique | [2025](calcul_scientifique/fr/numpy_scipy_matplotlib_2025.ipynb) | [2020](calcul_scientifique/en/numpy_scipy_matplotlib_2020.ipynb) | NumPy, SciPy, matplotlib et seaborn : complément au cours NumPy abrégé |

Les [tutoriels Git](../tutoriels/git/README.md) et les introductions Python en [français](../tutoriels/python/fr/python.ipynb) et en [anglais](../tutoriels/python/en/python.ipynb) sont rangés séparément. Les dossiers sources nommés `-fr` contenaient parfois des cours anglais; le classement ci-dessus suit la langue du contenu.

## Utilisation avec le dépôt actuel

Ces fichiers sont des **archives pédagogiques conservées sans modification du contenu**. Leur présence dans le dépôt ne signifie pas qu’ils ont été adaptés ou exécutés intégralement avec l’environnement actuel.

Le dépôt conserve un seul projet uv à la racine. Pour reprendre un ancien labo comme démo active, adaptez son code et ses données, puis ajoutez les dépendances nécessaires au `pyproject.toml` commun avant de le valider. N’ajoutez pas de projet uv dans chaque sous-dossier.

## Corrigés

Les [corrigés historiques](../solutions/anciens_labs/README.md) sont également disponibles. Leurs éditions et leurs limites sont indiquées dans leur index : ils ne correspondent pas tous exactement aux cours les plus récents.
