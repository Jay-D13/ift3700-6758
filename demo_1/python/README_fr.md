# Configuration de Python : venv manuel, puis uv

**Atelier facultatif dans une copie séparée.** Pour exécuter les notebooks du cours, suivez la [configuration commune du dépôt](../../README.md) : un seul `uv sync` depuis `ift3700-6758` suffit. Pour l’atelier ci-dessous, copiez le dossier `demo_1` complet **hors du dépôt**, en conservant son nom. Toutes les mentions de `demo_1` ci-dessous désignent cette copie séparée. L’exercice crée puis supprime sa propre `.venv`; il ne sert pas à configurer l’environnement partagé du cours.

**Exécutez toutes les commandes du terminal depuis `demo_1`, le dossier contenant `python/` et `notebooks/`.** Ouvrez ce dossier complet dans votre éditeur. Si votre terminal se trouve dans `demo_1/python`, exécutez une fois `cd ..`.

Les deux méthodes utilisent `demo_1/.venv`. Les scripts restent dans `python/`; les notebooks en français se trouvent dans `notebooks/fr/` et ceux en anglais dans `notebooks/en/`.

Avant le cours, installez **Python 3** et les extensions **Python** et **Jupyter** de VS Code. Nous installerons uv à l’étape 6. Commencez sans environnement activé.

Pour reprendre la démonstration depuis le début, utilisez une copie sans les fichiers d’environnement et de configuration générés. Si vous avez déjà `pyproject.toml` et `uv.lock` et souhaitez simplement exécuter les notebooks, passez à **Reprendre le projet plus tard**.

## Phase 1 : configuration manuelle

### 1. Créer l’environnement

macOS / Linux :

```sh
python3 --version
python3 -m venv .venv
```

Windows PowerShell :

```powershell
py -3 --version
py -3 -m venv .venv
```

La version affichée doit être Python 3.x. Cette commande crée `.venv` avec ce Python, sans l’activer.

**Que signifie `-m` ?** Cette option exécute un module Python comme un programme, avec l’interpréteur sélectionné. Ici, `python3 -m venv` lance le module de création d’environnement de Python. Plus loin, `python -m pip` lance pip avec le Python de l’environnement activé.

### 2. Activer l’environnement

macOS / Linux :

```sh
source .venv/bin/activate
```

Windows PowerShell :

```powershell
.\.venv\Scripts\Activate.ps1
```

Vérifiez :

```sh
python -c "import sys; print(sys.executable)"
```

**Que signifie `-c` ?** Cette option exécute directement le code Python entre guillemets, sans fichier `.py`. Ici, le code importe `sys` et affiche le chemin de l’exécutable Python qui le fait fonctionner.

Le chemin doit se trouver dans `demo_1/.venv`. L’activation s’applique uniquement à ce terminal.

Si PowerShell bloque l’activation, utilisez l’invite de commandes avec `.venv\Scripts\activate.bat`, ou remplacez `python` dans les commandes suivantes par `.\.venv\Scripts\python.exe`.

### 3. Installer les paquets et vérifier

```sh
python -m pip install numpy pandas
python python/check_environment.py
```

`python -m pip` installe les paquets dans l’environnement Python sélectionné. La vérification doit se terminer par **PASS**.

L’activation est facultative si vous indiquez directement le chemin de l’interpréteur : `.venv/bin/python python/check_environment.py` sur macOS/Linux, ou `.\.venv\Scripts\python.exe python/check_environment.py` sur Windows.

### 4. Enregistrer les versions installées

```sh
python -m pip freeze > requirements-venv.txt
```

Cette commande enregistre les versions installées dans un fichier à la racine du projet. Ce relevé conserve l’état de l’installation manuelle.

## Phase 2 : remise à zéro

### 5. Désactiver et supprimer l’environnement

Fermez les programmes qui utilisent l’environnement, puis exécutez `deactivate` (ignorez cette commande si vous ne l’avez jamais activé).

macOS / Linux :

```sh
python3 python/reset_environment.py
```

Windows PowerShell :

```powershell
py -3 python/reset_environment.py
```

Le script supprime uniquement `demo_1/.venv`. Les scripts, les notebooks et le relevé des versions sont conservés. Exécutez-le avec le Python de base, jamais avec `uv run`.

## Phase 3 : reconstruire avec uv

**Restez dans `demo_1`.** uv créera l’environnement partagé par les scripts et les notebooks.

### 6. Installer uv

Ignorez l’installation si `uv --version` fonctionne déjà.

macOS / Linux ([programme d’installation d’Astral](https://docs.astral.sh/uv/getting-started/installation/)) :

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows PowerShell :

```powershell
winget install --id=astral-sh.uv -e
```

Rouvrez votre terminal, revenez dans `demo_1`, puis vérifiez :

```sh
uv --version
```

### 7. Initialiser le projet une seule fois

```sh
uv init --bare --python 3
```

Cette commande crée `pyproject.toml` à la racine à partir d’un interpréteur Python 3 disponible. Ignorez `uv init` si `pyproject.toml` existe déjà.

**Pourquoi `--bare` ?** Cette option crée uniquement un fichier `pyproject.toml` minimal, sans code de départ, README, fichier `.python-version` ni initialisation de Git. La commande `uv init` seule fonctionne aussi, mais crée un projet de départ plus complet. Nous utilisons `--bare` parce que cette démonstration possède déjà ses scripts, ses notebooks et son README. Aucune des deux commandes n’installe encore les dépendances : cela se fait à l’étape suivante.

### 8. Ajouter les paquets et vérifier

```sh
uv add numpy pandas
uv run python/check_environment.py
```

`uv add` enregistre les dépendances, crée `uv.lock` et reconstruit `.venv`. La vérification doit de nouveau se terminer par **PASS**. Aucune activation n’est nécessaire.

| Fichier / dossier | Rôle |
|---|---|
| `pyproject.toml` | Besoins du projet |
| `uv.lock` | Versions résolues des dépendances |
| `.venv/` | Environnement installé, qui peut être recréé |

## Phase 4 : utiliser les notebooks

### 9. Ajouter les paquets pour les notebooks

```sh
uv add --dev ipykernel jupyterlab
uv add matplotlib scikit-learn
```

### 10. Sélectionner l’environnement dans VS Code

1. Ouvrez le dossier `demo_1` complet.
2. Lancez **Python: Select Interpreter** depuis la palette de commandes et sélectionnez la `.venv` à la racine.
3. Ouvrez un notebook dans `notebooks/fr/` (français) ou `notebooks/en/` (anglais).
4. Utilisez **Select Kernel → Python Environments** et sélectionnez cette même `.venv`.

Dans une cellule du notebook, vérifiez :

```python
import sys
import numpy as np
import pandas as pd

print(sys.executable)
assert np.mean([1, 2, 3]) == 2
assert pd.Series([1, 2, 3]).sum() == 6
```

L’interpréteur doit se trouver dans `demo_1/.venv`. Si les imports échouent, vérifiez le noyau sélectionné et redémarrez-le.

### 11. Autre possibilité dans le navigateur : JupyterLab

Depuis `demo_1` :

```sh
uv run jupyter lab
```

Ouvrez un notebook dans `notebooks/fr/` (français) ou `notebooks/en/` (anglais) et sélectionnez le noyau Python du projet. Arrêtez le serveur avec `Ctrl+C`.

### 12. Conserver les fichiers du projet

Ajoutez ces lignes à `demo_1/.gitignore` :

```gitignore
.venv/
__pycache__/
.ipynb_checkpoints/
.env
```

Enregistrez dans Git les scripts, les notebooks, `pyproject.toml`, `uv.lock` et `.gitignore`. Conservez le relevé de l’installation manuelle pour comparer.

## Reprendre le projet plus tard

Depuis `demo_1` :

```sh
uv sync --locked
uv run python/check_environment.py
```

Ouvrez ensuite votre notebook et sélectionnez le noyau de la `.venv` à la racine. Utilisez `uv add` pour ajouter des paquets; n’initialisez pas le projet à nouveau.

Références : [options de la ligne de commande Python](https://docs.python.org/3/using/cmdline.html#interface-options) · [création de projets avec uv](https://docs.astral.sh/uv/concepts/projects/init/) · [uv avec Jupyter](https://docs.astral.sh/uv/guides/integration/jupyter/)
