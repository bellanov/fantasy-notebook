#!/bin/bash
#
# Format Code Base.

# Format Imports
echo "Formatting imports..."
isort python_template
isort tests

# Format Code
echo "Formatting code base..."
black python_template 

# Format Tests
echo "Formatting tests..."
black tests
