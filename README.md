# everything is a metric
collecting metrics for everything over GET and PUSH requests and offering a /metrics endpoint for prometheus

## Endpoints

```bash
GET     /                   display info page
GET     /metrics            display metrics
GET     /metric/<key>       display just the value of <key>
PUSH    /increment/<key>    increment the value of <key>
```

## Storage

The metrics are stored in a json file, in the data folder. The file is created if it doesn't exist.

## Configuration

All configuration is done via environment variables. Currently is only one variable used:

```bash
ENV                 default         description
allowNewMetrics     true            wether to allow new metrics to be created via the /increment endpoint or not
```

## Development

To keep the dependencies clean, we use a virtual environment. To create one, run the following commands:

```bash
python3 -m pip install --user virtualenv
```

```bash
python3 -m venv env
source venv/bin/activate # or . env/bin/activate
which python
```

```bash
pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

