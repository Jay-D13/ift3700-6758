# Démo 2 : acquisition, exploration et analyse des données NHL

[English version](README_en.md)

Cette démo utilise les données d’un match Montréal–Caroline pour apprendre à récupérer et nettoyer des données, les explorer visuellement, puis utiliser un LLM pour aider à écrire du code et à analyser une table.

## Notebooks

| Notebook | Ce qu’on apprend et réalise | Français | English |
|---|---|---|---|
| **01 — Acquisition et nettoyage** | Comprendre une requête d’API, télécharger et sauvegarder le JSON d’un match, puis le transformer en table pandas. Conserver les tirs et les buts, vérifier les identifiants et les valeurs manquantes, puis exporter un CSV. | [Ouvrir](notebooks/fr/01_data_acquisition_and_cleaning.ipynb) | [Open](notebooks/en/01_data_acquisition_and_cleaning.ipynb) |
| **02 — Exploration et visualisation** | Examiner les événements bruts et leur position sur une patinoire avec des widgets. Rejouer les tirs et les buts, comparer les tirs cumulés avec Plotly et exporter un graphique interactif en HTML. | [Ouvrir](notebooks/fr/02_data_exploration_and_visualization.ipynb) | [Open](notebooks/en/02_data_exploration_and_visualization.ipynb) |
| **04 — LLM et RAG** | Comprendre comment le RAG fournit des passages de documentation à un LLM. Rechercher dans la documentation de l’API NHL avec MiniLM et FAISS, puis demander à Qwen une fonction d’acquisition et vérifier son code et sa mise en cache. | [Ouvrir](notebooks/fr/04_llm_and_rag.ipynb) | [Open](notebooks/en/04_llm_and_rag.ipynb) |
| **05 — PandasAI** | Interroger une table en langage naturel avec PandasAI et Qwen pour obtenir un nombre, un tableau et un graphique. Examiner le code généré et comparer les résultats avec des calculs pandas. | [Ouvrir](notebooks/fr/05_pandasai.ipynb) | [Open](notebooks/en/05_pandasai.ipynb) |

Commencez par le notebook **01**, puis poursuivez dans l’ordre du tableau. Chaque notebook contient ses instructions de configuration et d’exécution; la [configuration commune du cours](../README.md) sert de référence pour l’environnement local.

## Matériel conseillé pour les notebooks 04 et 05

Pour ces notebooks avec **Qwen2.5-1.5B-Instruct**, nous recommandons **Google Colab avec un GPU T4** si vous n’avez pas de GPU NVIDIA adapté ou de Mac avec une puce Apple M. Suivez les instructions Colab du notebook.

Pour travailler en local, visez **8 Go de VRAM sur un GPU NVIDIA** ou **16 Go de mémoire unifiée sur un Mac avec une puce M**. Ce sont des repères de confort, pas des minimums stricts : les besoins varient selon la longueur des prompts et la quantification. Les [mesures publiées par Qwen](https://qwen.readthedocs.io/en/v2.5/benchmark/speed_benchmark.html) donnent environ 3 à 6 Go pour le modèle en BF16 selon le contexte; prévoyez aussi de la mémoire pour le reste du notebook. L’exécution sur CPU reste possible, mais plus lente.

<sub>Préparé par Jaydan Aladro and Pablo Boitel</sub>