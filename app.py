import os
import json
app = Flask(__name__)
strichliste = {}
strichliste = load_strichliste()

@app.route('/increment/<name>', methods=['POST'])
def increment_count(name):
    global strichliste

    if name in strichliste:
        strichliste[name] += 1
    else:
        strichliste[name] = 1

    save_strichliste()

    requests_counter.inc()

    return 'OK', 200
