#!/bin/bash

set -e # Exits on any errors

# Check Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Installing..."
    sudo apt install python3
fi

# Create virtual environment
echo "Creating virtual environment..."
python -m venv .venv

# Activate virtual environment
if [[ "$(uname -s)" == "Darwin" ]]; then
    source ./venv/bin/activate
else
    source ./.venv/Scripts/activate
fi

./run2.sh