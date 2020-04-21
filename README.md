# sketchmoji
A stroke-based emoji sketch recognizer


In order to run the python server locally

make virual env (replace python3 with your python path)
virtualenv -p python3 venv

activate it using
source venv/bin/activate

pip install flask
pip install -U flask-cors
pip install -r src/requirements.txt


export FLASK_APP=src/basicserver.py

and then to run the server use 

flask run

Once the server is running the interface in the file index.html will call it and be able to classify the sketches