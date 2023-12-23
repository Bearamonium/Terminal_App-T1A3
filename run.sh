#!/bin/bash

set -e # Exits on any errors

# Check operating system
os_name="$(uname -s)"

# Check for Python based on OS
if [[ "$os_name" == "Linux" ]]; then
    # Linux:
    if ! command -v python3 &> /dev/null; then
        echo "Python 3 is not installed. Installing..."
        sudo apt install python3  # Adjust package manager if needed
    fi
elif [[ "$os_name" == "Darwin" ]]; then
    # macOS:
    if ! command -v python3 &> /dev/null; then
        echo "Python 3 is not installed."
        if ! command -v brew &> /dev/null; then
            echo "Homebrew is not installed either. Please install Homebrew first from https://brew.sh/"
            exit 1
        else
            echo "Installing Python using Homebrew..."
            brew install python3
        fi
    fi
else
    # Windows:
    echo "Python installation is required for Windows. Please follow the steps at https://www.python.org/downloads/windows/"
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv .venv

source ./.venv/bin/activate

./run2.sh