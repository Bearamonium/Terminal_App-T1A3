#!/bin/bash

pip install -r requirements.txt

python ./source_code/main.py

#Cleanup
deactivate
rm -rf .venv

echo "Game finished! Thanks for playing."