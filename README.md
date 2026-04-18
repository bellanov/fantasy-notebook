# Python Template

Template for general `Python` development.

## Development Workflow

First, a local project environment needs to be created, then the project's modules will be installed into locally into a virtual environment.

1. Clone the repository.

   ```sh
   git clone https://github.com/bellanov/python-template.git
   cd python-template
   ```

2. Create a virtual environment.

   ```sh
   # Create Virtual Environment
   python3 -m venv .venv

   # Activate Virtual Environment
   source .venv/bin/activate

   # Install Dependencies
   pip install -r requirements.txt 

   # Deactivate Virtual Environment
   deactivate
   ```

3. Make your changes, increment the version in `pyproject.toml`, and open a **Pull Request**.

   ```sh
   # Create a branch to isolate your changes
   git branch my-new-feature

   # Hop onto the branch to add your changes
   git checkout my-new-feature

   # Make your changes and commit them
   git add .
   git commit -m "Added My New Feature"

   # Push the changes to your branch (first push)
   git push --set-upstream origin my-new-feature

   # All future pushes
   git push

   # Create a pull request using the provided link after pushing
   remote: 
   remote: Create a pull request for 'my-new-feature' on GitHub by visiting:
   remote:      https://github.com/bellanov/python-template/pull/new/my-new-feature

   # Rev the version in pyproject.toml and tag the changes
   git tag -a "0.1.0" -m "Version 0.1.0"

   # Push the tags
   git push --follow-tags
   ```

## Testing, Linting, and Formatting

Be sure to constantly *test*, *lint*, and *format* the code base while developing.

```sh
# Execute Unit Tests
scripts/test.sh

# Lint Code Base
scripts/lint.sh
```
