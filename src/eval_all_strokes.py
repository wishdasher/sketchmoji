import matplotlib.pyplot as plt

from stroke_segmentation import segment_stroke
from plot_segmentation import plot_segmentation
from Stroke import Stroke
from stroke_data import strokes
from classify_strokes import classify_stroke
from template_data import get_templates
#list of all Templates
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

custom_strokes = strokes
# plt.figure(1, figsize=(12, 8))
strokeNumber = 1
for cs in custom_strokes:
    strk = Stroke(x=cs['x'], y=cs['y'], t=cs['t'])
    best_match = classify_stroke(strk, templates)
    print(f"{bcolors.BOLD}", "STROKE NUMBER:", strokeNumber, f"{bcolors.ENDC}")
    print(f"{bcolors.BOLD}", "STROKE CLASS:", stroke_names[strokeNumber], f"{bcolors.ENDC}")
    if best_match == stroke_names[strokeNumber]:
        print(f"{bcolors.BOLD}", "YOUR CLASSIFICATION:", f"{bcolors.OKGREEN}", best_match, f"{bcolors.ENDC}", f"{bcolors.ENDC}")
    else:
        print(f"{bcolors.BOLD}", "YOUR CLASSIFICATION:", f"{bcolors.FAIL}", best_match, f"{bcolors.ENDC}", f"{bcolors.ENDC}")



    clean_segment_indices, segtypes = segment_stroke(strk)
    # plot_segmentation(strk, clean_segment_indices, segtypes, all=True)
    strokeNumber +=1


# plt.figure(1).canvas.set_window_title('MIT 6.835: Stroke Segmentation')
# plt.tight_layout()
# plt.show()
