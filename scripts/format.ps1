#!/bin/bash
#
# Format Code Base.

# Format Imports
echo "Formatting imports..."
isort fantasy_notebook
isort tests

# Format Code
echo "Formatting code base..."
black fantasy_notebook 

# Format Tests
echo "Formatting tests..."
black tests
