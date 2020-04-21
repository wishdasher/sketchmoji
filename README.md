# SketchMoji

A stroke-based emoji sketch recognizer

## Local setup

Clone the repo and run the python server

Create the virtual environment.

```
virtualenv -p python3 venv
source venv/bin/activate
```

Install dependencies.

```
pip install flask
pip install -U flask-cors
pip install -r src/requirements.txt
export FLASK_APP=src/basicserver.py
```

Run the server.

```
flask run
```

Once the server is running, open 'http://127.0.0.1:5000/sketchmoji' in your browser
