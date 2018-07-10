#! usr/bin/env python3
# coding: utf-8

from dotenv import load_dotenv
import os

file_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(file_path, os.path.pardir))

env_path = os.path.join(project_path, 'resources/.env')
load_dotenv(verbose=True, dotenv_path=env_path)

DIALOGFLOW_TOKEN = os.getenv("DIALOGFLOW_TOKEN")