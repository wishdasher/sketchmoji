import sys

import matplotlib.pyplot as plt

from stroke_segmentation import segment_stroke
from plot_segmentation import plot_segmentation
from Stroke import Stroke
from stroke_data import strokes
from classify_strokes import classify_stroke
from template_data import get_templates

#List of all templates
templates = get_templates()

class bcolors:
    BOLD = '\033[1m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

stroke_names = {
                    1: "STRAIGHT LINE",
                    2: "CURVE",
                    3: "SKEWED CIRCLE",
                    4: "TWO MOUNTAINS",
                    5: "OMEGA",
                    6: "TRIANGLE",
                    7: "SIGMA",
                    8: "FIVE",
                    9: "THREE FEATHERS",
                    10: "CHEF HAT",
                    11: "DOME",
                    12: "MUSIC NOTE"
                }

if len(sys.argv) != 2:
    raise ValueError('Error! Give stroke number after filename in command. \n e.g. python eval_stroke.py 2')

i = int(sys.argv[1])

if i <= len(strokes) and i > 0 or i == -1:
    strokeNumber = i
    cs = strokes[i-1]
    strk = Stroke(x=cs['x'], y=cs['y'], t=cs['t'])
    clean_segment_indices, segtypes = segment_stroke(strk)
    best_match = classify_stroke(strk, templates)

    print(f"{bcolors.BOLD}", "STROKE NUMBER:", strokeNumber, f"{bcolors.ENDC}")
    print(f"{bcolors.BOLD}", "STROKE CLASS:", stroke_names[strokeNumber], f"{bcolors.ENDC}")
    if best_match == stroke_names[strokeNumber]:
        print(f"{bcolors.BOLD}", "YOUR CLASSIFICATION:", f"{bcolors.OKGREEN}", best_match, f"{bcolors.ENDC}", f"{bcolors.ENDC}")
    else:
        print(f"{bcolors.BOLD}", "YOUR CLASSIFICATION:", f"{bcolors.FAIL}", best_match, f"{bcolors.ENDC}", f"{bcolors.ENDC}")

    plot_segmentation(strk, clean_segment_indices, segtypes)
    plt.figure(1).canvas.set_window_title('MIT 6.835: Stroke Segmentation')
    plt.show()
else:
    msg = 'Stroke index out of range. Give a number between 1 and ' + str(strokes.size)
    raise ValueError(msg)
