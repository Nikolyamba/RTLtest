import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "videos.json")

with open(DATA_PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)