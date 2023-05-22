import os
import json
from functions import load_strichliste, save_strichliste, generate_metrics

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

@app.route('/')
def info():
    return render_template('info.html')

def main():
    app.run(debug=False, host='0.0.0.0', port=3400)

if __name__ == '__main__':
    main()
