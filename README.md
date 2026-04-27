# Fantasy Notebook

Notebook for exploring sports betting data.

## Quickstart

First, a local project environment needs to be created, then the project's modules will be installed into locally into a virtual environment.

1. Clone the repository.

   ```sh
   git clone https://github.com/bellanov/fantasy_notebook.git
   cd fantasy_notebook
   ```

2. Create a virtual environment.

   ```sh
   # Create Virtual Environment
   python3 -m venv .venv

   # Activate Virtual Environment
   source .venv/bin/activate

   # Install Dependencies
   pip install -r requirements.txt -r dev-requirements.txt

   # Deactivate Virtual Environment
   deactivate
   ```

## Testing

Execute unit tests to validate the installation.

```sh
# Execute Unit Tests
scripts/test.sh
```

## Execute Notebook

Execute any of the Notebooks in the `notebooks/` directory using *Marimo*.

```sh
marimo run sports.py
```
