#!/usr/bin/env bash

virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
cd core
python CLUI.py

deactivate
rm -rf venv