import os
import json
def load_strichliste():
    global strichliste
    try:
        with open('data/strichliste.json', 'r') as file:
            strichliste = json.load(file)
            print("Loaded successfully")
    except FileNotFoundError:
        strichliste = {}
        print("File not found, starting new one")

    return strichliste

def save_strichliste():
    with open('data/strichliste.json', 'w') as file:
        json.dump(strichliste, file)
