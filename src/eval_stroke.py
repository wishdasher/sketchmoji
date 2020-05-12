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
    # cs = strokes[i-1]
    # cs = {'x': [[224.6171875, 223.6171875, 223.6171875, 223.6171875, 222.6171875, 220.6171875, 217.6171875, 215.6171875, 213.6171875, 210.6171875, 207.6171875, 205.6171875, 202.6171875, 201.6171875, 199.6171875, 198.6171875, 197.6171875, 196.6171875, 195.6171875, 194.6171875, 193.6171875, 193.6171875, 192.6171875, 191.6171875, 191.6171875, 190.6171875, 189.6171875, 188.6171875, 186.6171875, 185.6171875, 183.6171875, 182.6171875, 181.6171875, 181.6171875, 179.6171875, 179.6171875, 178.6171875, 177.6171875, 176.6171875, 174.6171875, 172.6171875, 170.6171875, 167.6171875, 164.6171875, 159.6171875, 157.6171875, 153.6171875, 152.6171875, 150.6171875, 150.6171875, 151.6171875, 160.6171875, 171.6171875, 186.6171875, 194.6171875, 203.6171875, 204.6171875, 203.6171875, 187.6171875, 174.6171875, 164.6171875, 158.6171875, 153.6171875, 151.6171875, 150.6171875, 149.6171875, 149.6171875, 149.6171875, 148.6171875, 148.6171875, 148.6171875, 148.6171875, 148.6171875, 151.6171875, 156.6171875, 165.6171875, 175.6171875, 186.6171875, 198.6171875, 204.6171875, 210.6171875, 215.6171875, 218.6171875, 221.6171875, 225.6171875, 230.6171875, 235.6171875, 243.6171875, 250.6171875, 258.6171875, 266.6171875, 272.6171875, 281.6171875, 286.6171875, 293.6171875, 298.6171875, 302.6171875, 306.6171875, 310.6171875, 313.6171875, 316.6171875, 319.6171875, 322.6171875, 325.6171875, 328.6171875, 332.6171875, 336.6171875, 340.6171875, 343.6171875, 345.6171875, 348.6171875, 349.6171875, 350.6171875, 351.6171875, 352.6171875, 353.6171875, 353.6171875, 354.6171875, 356.6171875, 359.6171875, 363.6171875, 366.6171875, 368.6171875, 371.6171875, 375.6171875, 376.6171875, 378.6171875, 379.6171875, 380.6171875, 380.6171875, 380.6171875, 380.6171875, 380.6171875, 380.6171875, 380.6171875, 379.6171875, 378.6171875, 377.6171875, 375.6171875, 375.6171875, 373.6171875, 372.6171875, 370.6171875, 367.6171875, 363.6171875, 356.6171875, 345.6171875, 331.6171875, 319.6171875, 311.6171875, 304.6171875, 300.6171875, 300.6171875, 300.6171875, 301.6171875, 303.6171875, 304.6171875, 304.6171875, 301.6171875, 295.6171875, 287.6171875, 277.6171875, 265.6171875, 247.6171875, 241.6171875, 226.6171875, 221.6171875, 215.6171875, 211.6171875, 208.6171875, 207.6171875, 205.6171875, 204.6171875, 202.6171875]], 'y': [[120.91015625, 120.91015625, 120.91015625, 120.91015625, 120.91015625, 122.91015625, 125.91015625, 129.91015625, 134.91015625, 139.91015625, 145.91015625, 150.91015625, 155.91015625, 159.91015625, 163.91015625, 166.91015625, 169.91015625, 174.91015625, 177.91015625, 180.91015625, 183.91015625, 185.91015625, 188.91015625, 190.91015625, 191.91015625, 194.91015625, 196.91015625, 198.91015625, 200.91015625, 203.91015625, 206.91015625, 209.91015625, 211.91015625, 213.91015625, 215.91015625, 217.91015625, 219.91015625, 222.91015625, 224.91015625, 227.91015625, 229.91015625, 231.91015625, 234.91015625, 236.91015625, 240.91015625, 243.91015625, 246.91015625, 250.91015625, 254.91015625, 257.91015625, 260.91015625, 261.91015625, 261.91015625, 259.91015625, 259.91015625, 259.91015625, 263.91015625, 277.91015625, 307.91015625, 332.91015625, 349.91015625, 359.91015625, 365.91015625, 368.91015625, 369.91015625, 370.91015625, 371.91015625, 372.91015625, 373.91015625, 374.91015625, 376.91015625, 378.91015625, 379.91015625, 379.91015625, 379.91015625, 377.91015625, 375.91015625, 375.91015625, 375.91015625, 375.91015625, 375.91015625, 375.91015625, 375.91015625, 375.91015625, 375.91015625, 375.91015625, 375.91015625, 375.91015625, 375.91015625, 373.91015625, 372.91015625, 370.91015625, 369.91015625, 367.91015625, 366.91015625, 365.91015625, 364.91015625, 362.91015625, 361.91015625, 359.91015625, 358.91015625, 356.91015625, 354.91015625, 352.91015625, 350.91015625, 348.91015625, 345.91015625, 343.91015625, 340.91015625, 338.91015625, 335.91015625, 334.91015625, 333.91015625, 333.91015625, 332.91015625, 331.91015625, 331.91015625, 329.91015625, 328.91015625, 325.91015625, 322.91015625, 318.91015625, 315.91015625, 312.91015625, 307.91015625, 304.91015625, 301.91015625, 299.91015625, 296.91015625, 294.91015625, 291.91015625, 290.91015625, 288.91015625, 286.91015625, 284.91015625, 282.91015625, 281.91015625, 278.91015625, 276.91015625, 274.91015625, 271.91015625, 267.91015625, 263.91015625, 258.91015625, 254.91015625, 250.91015625, 249.91015625, 249.91015625, 251.91015625, 256.91015625, 259.91015625, 260.91015625, 253.91015625, 233.91015625, 215.91015625, 192.91015625, 181.91015625, 165.91015625, 159.91015625, 153.91015625, 145.91015625, 137.91015625, 130.91015625, 123.91015625, 121.91015625, 116.91015625, 114.91015625, 111.91015625, 109.91015625, 107.91015625, 107.91015625, 106.91015625, 105.91015625, 105.91015625]], 't': [[1589264172488, 1589264172489, 1589264172696, 1589264172704, 1589264172721, 1589264172737, 1589264172753, 1589264172771, 1589264172787, 1589264172804, 1589264172820, 1589264172837, 1589264172854, 1589264172871, 1589264172888, 1589264172904, 1589264172921, 1589264172937, 1589264172955, 1589264172971, 1589264172988, 1589264173005, 1589264173020, 1589264173037, 1589264173055, 1589264173071, 1589264173087, 1589264173105, 1589264173120, 1589264173137, 1589264173154, 1589264173172, 1589264173187, 1589264173205, 1589264173221, 1589264173237, 1589264173254, 1589264173271, 1589264173288, 1589264173304, 1589264173321, 1589264173338, 1589264173354, 1589264173370, 1589264173387, 1589264173404, 1589264173421, 1589264173437, 1589264173455, 1589264173471, 1589264173488, 1589264173504, 1589264173522, 1589264173538, 1589264173554, 1589264173571, 1589264173587, 1589264173604, 1589264173621, 1589264173637, 1589264173655, 1589264173670, 1589264173688, 1589264173705, 1589264173721, 1589264173737, 1589264173754, 1589264173772, 1589264173788, 1589264173804, 1589264173821, 1589264173838, 1589264173854, 1589264173871, 1589264173887, 1589264173905, 1589264173921, 1589264173938, 1589264173955, 1589264173971, 1589264173988, 1589264174005, 1589264174021, 1589264174038, 1589264174054, 1589264174071, 1589264174088, 1589264174105, 1589264174121, 1589264174139, 1589264174155, 1589264174171, 1589264174187, 1589264174203, 1589264174221, 1589264174237, 1589264174254, 1589264174271, 1589264174287, 1589264174304, 1589264174321, 1589264174338, 1589264174355, 1589264174371, 1589264174387, 1589264174407, 1589264174422, 1589264174439, 1589264174455, 1589264174471, 1589264174488, 1589264174505, 1589264174522, 1589264174539, 1589264174554, 1589264174572, 1589264174588, 1589264174604, 1589264174622, 1589264174647, 1589264174671, 1589264174688, 1589264174704, 1589264174720, 1589264174739, 1589264174755, 1589264174772, 1589264174788, 1589264174804, 1589264174822, 1589264174837, 1589264174854, 1589264174873, 1589264174889, 1589264174905, 1589264174921, 1589264174938, 1589264174955, 1589264174971, 1589264174988, 1589264175006, 1589264175022, 1589264175039, 1589264175054, 1589264175073, 1589264175088, 1589264175105, 1589264175122, 1589264175139, 1589264175155, 1589264175171, 1589264175188, 1589264175204, 1589264175221, 1589264175238, 1589264175255, 1589264175272, 1589264175289, 1589264175305, 1589264175323, 1589264175338, 1589264175355, 1589264175371, 1589264175388, 1589264175405, 1589264175421, 1589264175438, 1589264175455, 1589264175472, 1589264175496, 1589264175505, 1589264175522, 1589264175538, 1589264175554]]}
    cs = {'x': [[258.6171875, 258.6171875, 257.6171875, 255.6171875, 252.6171875, 248.6171875, 244.6171875, 241.6171875, 237.6171875, 234.6171875, 230.6171875, 225.6171875, 218.6171875, 210.6171875, 203.6171875, 197.6171875, 194.6171875, 192.6171875, 191.6171875, 191.6171875, 191.6171875, 191.6171875, 193.6171875, 196.6171875, 199.6171875, 202.6171875, 205.6171875, 208.6171875, 210.6171875, 211.6171875, 211.6171875, 212.6171875, 212.6171875, 210.6171875, 206.6171875, 202.6171875, 194.6171875, 185.6171875, 176.6171875, 167.6171875, 159.6171875, 152.6171875, 147.6171875, 142.6171875, 138.6171875, 136.6171875, 134.6171875, 131.6171875, 129.6171875, 127.6171875, 126.6171875, 125.6171875, 124.6171875, 123.6171875, 123.6171875, 123.6171875, 123.6171875, 123.6171875, 125.6171875, 127.6171875, 131.6171875, 140.6171875, 149.6171875, 155.6171875, 163.6171875, 169.6171875, 174.6171875, 177.6171875, 180.6171875, 183.6171875, 186.6171875, 188.6171875, 191.6171875, 193.6171875, 197.6171875, 200.6171875, 201.6171875, 203.6171875, 205.6171875, 206.6171875, 207.6171875, 207.6171875, 207.6171875, 207.6171875, 207.6171875, 206.6171875, 203.6171875, 199.6171875, 195.6171875, 189.6171875, 184.6171875, 178.6171875, 173.6171875, 168.6171875, 161.6171875, 155.6171875, 150.6171875, 145.6171875, 141.6171875, 137.6171875, 135.6171875, 133.6171875, 131.6171875, 131.6171875, 131.6171875, 131.6171875, 131.6171875, 131.6171875, 132.6171875, 136.6171875, 142.6171875, 153.6171875, 174.6171875, 198.6171875, 223.6171875, 253.6171875, 272.6171875, 290.6171875, 305.6171875, 318.6171875, 330.6171875, 342.6171875, 352.6171875, 359.6171875, 367.6171875, 374.6171875, 380.6171875, 385.6171875, 392.6171875, 396.6171875, 400.6171875, 403.6171875, 405.6171875, 406.6171875, 406.6171875, 406.6171875, 403.6171875, 399.6171875, 394.6171875, 388.6171875, 383.6171875, 378.6171875, 371.6171875, 361.6171875, 351.6171875, 343.6171875, 335.6171875, 328.6171875, 324.6171875, 321.6171875, 321.6171875, 321.6171875, 321.6171875, 321.6171875, 322.6171875, 324.6171875, 328.6171875, 329.6171875, 331.6171875, 332.6171875, 333.6171875, 333.6171875, 333.6171875, 333.6171875, 333.6171875, 333.6171875, 332.6171875, 331.6171875, 329.6171875, 325.6171875, 320.6171875, 315.6171875, 310.6171875, 305.6171875, 301.6171875, 298.6171875, 296.6171875, 294.6171875, 293.6171875, 292.6171875, 292.6171875, 291.6171875, 291.6171875, 291.6171875, 291.6171875, 291.6171875, 292.6171875, 292.6171875, 292.6171875, 292.6171875, 292.6171875, 292.6171875, 292.6171875, 291.6171875, 290.6171875, 289.6171875, 288.6171875, 285.6171875, 283.6171875, 280.6171875, 277.6171875, 275.6171875, 272.6171875, 270.6171875, 267.6171875, 264.6171875, 262.6171875, 261.6171875, 260.6171875, 258.6171875, 258.6171875]], 'y': [[124.91015625, 124.91015625, 124.91015625, 124.91015625, 124.91015625, 124.91015625, 124.91015625, 124.91015625, 126.91015625, 131.91015625, 136.91015625, 144.91015625, 157.91015625, 170.91015625, 184.91015625, 197.91015625, 207.91015625, 213.91015625, 221.91015625, 226.91015625, 231.91015625, 233.91015625, 234.91015625, 235.91015625, 237.91015625, 239.91015625, 241.91015625, 242.91015625, 244.91015625, 245.91015625, 246.91015625, 247.91015625, 248.91015625, 249.91015625, 250.91015625, 251.91015625, 253.91015625, 256.91015625, 259.91015625, 262.91015625, 266.91015625, 268.91015625, 270.91015625, 271.91015625, 273.91015625, 274.91015625, 275.91015625, 279.91015625, 281.91015625, 283.91015625, 286.91015625, 288.91015625, 290.91015625, 292.91015625, 294.91015625, 296.91015625, 297.91015625, 297.91015625, 298.91015625, 298.91015625, 299.91015625, 300.91015625, 301.91015625, 303.91015625, 304.91015625, 305.91015625, 306.91015625, 306.91015625, 307.91015625, 307.91015625, 307.91015625, 307.91015625, 308.91015625, 309.91015625, 309.91015625, 310.91015625, 311.91015625, 312.91015625, 312.91015625, 313.91015625, 314.91015625, 314.91015625, 315.91015625, 316.91015625, 318.91015625, 319.91015625, 321.91015625, 322.91015625, 323.91015625, 325.91015625, 327.91015625, 330.91015625, 333.91015625, 336.91015625, 339.91015625, 342.91015625, 344.91015625, 346.91015625, 348.91015625, 350.91015625, 351.91015625, 352.91015625, 355.91015625, 357.91015625, 359.91015625, 360.91015625, 363.91015625, 364.91015625, 365.91015625, 366.91015625, 367.91015625, 370.91015625, 373.91015625, 375.91015625, 377.91015625, 378.91015625, 378.91015625, 378.91015625, 378.91015625, 376.91015625, 372.91015625, 369.91015625, 365.91015625, 363.91015625, 360.91015625, 357.91015625, 355.91015625, 352.91015625, 348.91015625, 345.91015625, 342.91015625, 339.91015625, 337.91015625, 334.91015625, 331.91015625, 328.91015625, 324.91015625, 320.91015625, 316.91015625, 312.91015625, 310.91015625, 308.91015625, 307.91015625, 305.91015625, 304.91015625, 303.91015625, 301.91015625, 300.91015625, 299.91015625, 299.91015625, 298.91015625, 297.91015625, 296.91015625, 295.91015625, 293.91015625, 289.91015625, 280.91015625, 275.91015625, 268.91015625, 261.91015625, 255.91015625, 251.91015625, 247.91015625, 245.91015625, 244.91015625, 242.91015625, 241.91015625, 240.91015625, 239.91015625, 236.91015625, 234.91015625, 232.91015625, 230.91015625, 229.91015625, 228.91015625, 227.91015625, 226.91015625, 225.91015625, 224.91015625, 223.91015625, 222.91015625, 220.91015625, 218.91015625, 214.91015625, 211.91015625, 208.91015625, 202.91015625, 198.91015625, 193.91015625, 187.91015625, 181.91015625, 177.91015625, 173.91015625, 170.91015625, 168.91015625, 166.91015625, 164.91015625, 162.91015625, 160.91015625, 158.91015625, 156.91015625, 155.91015625, 153.91015625, 151.91015625, 149.91015625, 147.91015625, 145.91015625, 143.91015625, 141.91015625, 139.91015625, 138.91015625]], 't': [[1589265688900, 1589265689028, 1589265689040, 1589265689058, 1589265689074, 1589265689090, 1589265689106, 1589265689123, 1589265689140, 1589265689156, 1589265689173, 1589265689190, 1589265689206, 1589265689224, 1589265689241, 1589265689257, 1589265689274, 1589265689291, 1589265689307, 1589265689323, 1589265689340, 1589265689357, 1589265689373, 1589265689390, 1589265689407, 1589265689424, 1589265689441, 1589265689458, 1589265689474, 1589265689491, 1589265689508, 1589265689525, 1589265689541, 1589265689558, 1589265689573, 1589265689590, 1589265689607, 1589265689624, 1589265689641, 1589265689657, 1589265689675, 1589265689691, 1589265689707, 1589265689724, 1589265689741, 1589265689757, 1589265689774, 1589265689791, 1589265689808, 1589265689823, 1589265689841, 1589265689857, 1589265689875, 1589265689891, 1589265689907, 1589265689925, 1589265689941, 1589265689958, 1589265689974, 1589265689991, 1589265690008, 1589265690024, 1589265690040, 1589265690058, 1589265690074, 1589265690092, 1589265690106, 1589265690123, 1589265690141, 1589265690158, 1589265690175, 1589265690191, 1589265690207, 1589265690224, 1589265690241, 1589265690258, 1589265690273, 1589265690291, 1589265690309, 1589265690325, 1589265690341, 1589265690358, 1589265690374, 1589265690391, 1589265690411, 1589265690425, 1589265690441, 1589265690457, 1589265690473, 1589265690491, 1589265690507, 1589265690524, 1589265690540, 1589265690558, 1589265690575, 1589265690591, 1589265690607, 1589265690625, 1589265690642, 1589265690658, 1589265690674, 1589265690691, 1589265690707, 1589265690724, 1589265690741, 1589265690758, 1589265690775, 1589265690791, 1589265690808, 1589265690825, 1589265690842, 1589265690859, 1589265690875, 1589265690891, 1589265690908, 1589265690925, 1589265690941, 1589265690958, 1589265690975, 1589265690992, 1589265691008, 1589265691026, 1589265691041, 1589265691058, 1589265691075, 1589265691092, 1589265691109, 1589265691124, 1589265691141, 1589265691157, 1589265691175, 1589265691191, 1589265691208, 1589265691225, 1589265691241, 1589265691257, 1589265691274, 1589265691292, 1589265691307, 1589265691325, 1589265691341, 1589265691358, 1589265691374, 1589265691392, 1589265691409, 1589265691426, 1589265691441, 1589265691459, 1589265691475, 1589265691492, 1589265691508, 1589265691526, 1589265691542, 1589265691558, 1589265691575, 1589265691591, 1589265691609, 1589265691626, 1589265691642, 1589265691659, 1589265691675, 1589265691692, 1589265691708, 1589265691725, 1589265691741, 1589265691759, 1589265691775, 1589265691792, 1589265691808, 1589265691825, 1589265691841, 1589265691858, 1589265691876, 1589265691892, 1589265691909, 1589265691925, 1589265691942, 1589265691959, 1589265691975, 1589265691992, 1589265692009, 1589265692024, 1589265692041, 1589265692058, 1589265692074, 1589265692092, 1589265692108, 1589265692125, 1589265692142, 1589265692159, 1589265692175, 1589265692192, 1589265692209, 1589265692225, 1589265692242, 1589265692258, 1589265692275, 1589265692292, 1589265692309, 1589265692326, 1589265692342, 1589265692359, 1589265692376, 1589265692392, 1589265692408, 1589265692426, 1589265692443, 1589265692459, 1589265692475, 1589265692492, 1589265692509]]}
         # strk = Stroke(x=cs['x'], y=cs['y'], t=cs['t'])
    strks = [Stroke(x=cs['x'][i], y=cs['y'][i], t=cs['t'][i]) for i in range(len(cs['x']))]
    best_match = classify_stroke(strks, templates)
    for strk in strks:
        clean_segment_indices, segtypes = segment_stroke(strk)

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
