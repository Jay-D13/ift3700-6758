# Démo 2 : explorer un match NHL

Cette séance couvre l’acquisition, le nettoyage, l’exploration et la visualisation des événements d’un match NHL.

- [Notebook français](notebooks/fr/00_session.ipynb)
- [English notebook](notebooks/en/00_session.ipynb)

## Google Colab

1. Ouvrir [Google Colab](https://colab.research.google.com/) et importer le notebook choisi.
2. Sélectionner un runtime CPU, puis **Tout exécuter**.
3. Si Colab demande un redémarrage après l’installation avec `uv`, redémarrer la session et relancer toutes les cellules.

## Exécution locale

Depuis la racine du dépôt :

```sh
git pull --ff-only
uv sync
uv run jupyter lab
```

Choisir le noyau de la `.venv`, puis utiliser **Restart Kernel and Run All**.

## Déroulement

La séance part d’une requête API et d’un fichier JSON, construit une table pandas de tirs, permet d’examiner les événements sur une patinoire, puis crée un replay et une courbe de tirs cumulés.

Le premier lancement télécharge le match `2025030311` et le conserve dans `data/raw`. Les exécutions suivantes réutilisent ce cache. Un seul match sert à illustrer la méthode; il ne permet pas de conclure sur une équipe ou une saison entière.
