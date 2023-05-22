import os
import json
from prometheus_client import start_http_server, Counter, generate_latest, CollectorRegistry, Gauge

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

def generate_metrics():
    registry = CollectorRegistry()
    
    for key, value in strichliste.items():
        metric_name = f'everything_metrics_{key}'
        gauge = Gauge(metric_name, 'Custom key-value pair', registry=registry)
        gauge.set(value)
    
    return generate_latest(registry)