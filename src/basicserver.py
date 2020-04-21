from flask import Flask,request,render_template
from stroke_segmentation import segment_stroke
from plot_segmentation import plot_segmentation
from Stroke import Stroke
from stroke_data import strokes
from classify_strokes import classify_stroke
from template_data import get_templates
from flask_cors import CORS,cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/<int:i>')
def hello_world(i):
	templates = get_templates
	strokeNumber = i
	cs = strokes[i-1]
	strk = Stroke(x=cs['x'], y=cs['y'], t=cs['t'])
	clean_segment_indices, segtypes = segment_stroke(strk)
	best_match = classify_stroke(strk, templates)
	return best_match

@app.route('/',methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def take_in_request():
	data = request.get_json()
	templates = get_templates()
	strk = Stroke(x=data['x'], y=data['y'], t=data['t'])
	clean_segment_indices, segtypes = segment_stroke(strk)
	best_match = classify_stroke(strk, templates)
	return {"best": best_match }

@app.route("/sketchmoji")
def sketchmoji():
    return render_template('index.html')