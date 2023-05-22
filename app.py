import os
import json
from prometheus_client import start_http_server, Counter, generate_latest, CollectorRegistry, Gauge
from flask import Flask, request, Response, render_template, redirect
from functions import load_strichliste, save_strichliste, generate_metrics

app = Flask(__name__)
requests_counter = Counter('everything_requests_total', 'Total number of requests')

strichliste = {}
allow_new_keys = os.environ.get('allowNewKeys', 'True').lower() == 'true'
if allow_new_keys:
    print('allowNewKeys: New keys are allowed')
else:
    print('allowNewKeys: New keys are not allowed')

strichliste = load_strichliste()

@app.route('/increment/<name>', methods=['POST'])
def increment_count(name):
    global strichliste

    if not allow_new_keys and name not in strichliste:
        return 'New keys are not allowed', 400

    if name in strichliste:
        strichliste[name] += 1
    else:
        strichliste[name] = 1

    save_strichliste()

    requests_counter.inc()

    return 'OK', 200

## route for /status/ without key
@app.route('/metric/', methods=['GET'])
def without_key():
    increment_count('without_key')
    return redirect('/metric/without_key')

@app.route('/metric/<name>', methods=['GET'])
def get_count(name):
    global strichliste

    if name in strichliste:
        value = str(strichliste[name])
    else:
        value = 0

    return render_template('metric.html', key=name, value=value)

@app.route('/metrics')
def metrics():
    metrics_data = generate_metrics()
    return Response(metrics_data, mimetype='text/plain')

@app.route('/')
def info():
    return render_template('info.html')

def main():
    app.run(debug=False, host='0.0.0.0', port=3400)

if __name__ == '__main__':
    main()
