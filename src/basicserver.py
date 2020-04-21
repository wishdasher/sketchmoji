from flask import Flask
from stroke_segmentation import segment_stroke
from plot_segmentation import plot_segmentation
from Stroke import Stroke
from stroke_data import strokes
from classify_strokes import classify_stroke
from template_data import get_templates

app = Flask(__name__)

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
def take_in_request():
	data = request.get_json()
	return data    
