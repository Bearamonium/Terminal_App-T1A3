#!/usr/bin/env bash

set -e # Exits on any errors

# Check Python is installed
if $/! command -v python &> /dev/null; then
    echo "Python is not installed. Please install Python to run this game."
    echo "You can download Python from https://www.python.org/downloads/"
    echo "Follow the installation instructions for your operating system."
    exit 1
fi

# Create virtual environment
python -m venv .venv

if [[ "$(uname -s)" == "Darwin" ]]; then
    source ./venv/bin/activate
else
    source ./.venv/Scripts/activate
fi

# Install dependencies
pip install -r requirements.txt

# Run game
python main.py

#Cleanup
deactivate
rm -rf .venv

echo "Game finished! Thanks for playing."