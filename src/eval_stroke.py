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
    cs = {'x': [[308.4921875, 307.4921875, 307.4921875, 305.4921875, 300.4921875, 289.4921875, 274.4921875, 257.4921875, 236.4921875, 219.4921875, 200.4921875, 192.4921875, 183.4921875, 175.4921875, 166.4921875, 156.4921875, 146.4921875, 135.4921875, 125.4921875, 114.4921875, 105.4921875, 96.4921875, 89.4921875, 81.4921875, 72.4921875, 67.4921875, 64.4921875, 62.4921875, 59.4921875, 59.4921875, 59.4921875, 59.4921875, 59.4921875, 62.4921875, 65.4921875, 69.4921875, 74.4921875, 82.4921875, 89.4921875, 93.4921875, 103.4921875, 110.4921875, 117.4921875, 126.4921875, 135.4921875, 145.4921875, 156.4921875, 169.4921875, 182.4921875, 193.4921875, 210.4921875, 220.4921875, 230.4921875, 238.4921875, 247.4921875, 256.4921875, 266.4921875, 278.4921875, 288.4921875, 299.4921875, 309.4921875, 319.4921875, 330.4921875, 340.4921875, 351.4921875, 359.4921875, 367.4921875, 377.4921875, 385.4921875, 392.4921875, 398.4921875, 403.4921875, 407.4921875, 409.4921875, 411.4921875, 412.4921875, 413.4921875, 413.4921875, 413.4921875, 411.4921875, 408.4921875, 406.4921875, 402.4921875, 399.4921875, 396.4921875, 390.4921875, 387.4921875, 383.4921875, 378.4921875, 374.4921875, 370.4921875, 366.4921875, 362.4921875, 355.4921875, 351.4921875, 346.4921875, 341.4921875, 337.4921875, 333.4921875, 328.4921875, 320.4921875, 314.4921875, 305.4921875, 294.4921875, 285.4921875, 278.4921875, 269.4921875, 266.4921875, 264.4921875, 263.4921875], [176.4921875, 176.4921875, 176.4921875, 175.4921875, 175.4921875, 171.4921875, 169.4921875, 165.4921875, 162.4921875, 160.4921875, 157.4921875, 154.4921875, 153.4921875, 152.4921875, 152.4921875, 152.4921875, 153.4921875, 154.4921875, 156.4921875, 158.4921875, 160.4921875, 163.4921875, 167.4921875, 170.4921875, 173.4921875, 175.4921875, 177.4921875, 180.4921875, 182.4921875, 184.4921875, 185.4921875, 186.4921875, 187.4921875, 188.4921875, 188.4921875, 189.4921875, 189.4921875, 189.4921875, 190.4921875, 190.4921875, 191.4921875, 192.4921875, 193.4921875, 194.4921875, 196.4921875, 201.4921875, 206.4921875, 213.4921875, 218.4921875, 224.4921875, 229.4921875, 233.4921875, 236.4921875, 238.4921875, 239.4921875, 240.4921875, 240.4921875, 240.4921875, 239.4921875, 237.4921875, 235.4921875, 231.4921875, 228.4921875, 224.4921875, 219.4921875, 215.4921875, 211.4921875, 207.4921875, 202.4921875, 195.4921875, 190.4921875, 188.4921875, 185.4921875, 184.4921875, 183.4921875, 182.4921875, 182.4921875, 182.4921875], [298.4921875, 298.4921875, 298.4921875, 297.4921875, 295.4921875, 293.4921875, 291.4921875, 290.4921875, 288.4921875, 286.4921875, 286.4921875, 285.4921875, 285.4921875, 285.4921875, 285.4921875, 285.4921875, 285.4921875, 287.4921875, 288.4921875, 291.4921875, 295.4921875, 299.4921875, 302.4921875, 305.4921875, 308.4921875, 310.4921875, 312.4921875, 314.4921875, 316.4921875, 317.4921875, 318.4921875, 318.4921875, 318.4921875, 318.4921875, 318.4921875, 318.4921875, 318.4921875, 318.4921875, 318.4921875, 319.4921875, 321.4921875, 323.4921875, 326.4921875, 330.4921875, 334.4921875, 339.4921875, 344.4921875, 349.4921875, 353.4921875, 355.4921875, 357.4921875, 359.4921875, 360.4921875, 361.4921875, 361.4921875, 361.4921875, 361.4921875, 361.4921875, 359.4921875, 357.4921875, 354.4921875, 350.4921875, 345.4921875, 340.4921875, 336.4921875, 332.4921875, 329.4921875, 326.4921875, 321.4921875, 318.4921875, 314.4921875, 310.4921875, 306.4921875, 302.4921875, 301.4921875, 300.4921875, 299.4921875, 298.4921875, 298.4921875], [170.4921875, 170.4921875, 172.4921875, 177.4921875, 186.4921875, 203.4921875, 214.4921875, 233.4921875, 250.4921875, 268.4921875, 282.4921875, 291.4921875, 300.4921875, 307.4921875, 310.4921875, 312.4921875, 313.4921875, 313.4921875, 313.4921875, 313.4921875, 313.4921875, 311.4921875, 310.4921875, 307.4921875, 304.4921875, 301.4921875, 296.4921875, 293.4921875, 290.4921875, 286.4921875, 282.4921875, 278.4921875, 273.4921875, 269.4921875, 264.4921875, 258.4921875, 251.4921875, 244.4921875, 236.4921875, 226.4921875, 215.4921875, 201.4921875, 195.4921875, 189.4921875, 183.4921875, 181.4921875, 177.4921875, 174.4921875, 170.4921875, 168.4921875, 165.4921875, 162.4921875, 159.4921875, 158.4921875, 157.4921875, 157.4921875, 157.4921875, 158.4921875, 159.4921875, 160.4921875, 161.4921875, 161.4921875, 161.4921875]], 'y': [[141.91015625, 141.91015625, 141.91015625, 141.91015625, 141.91015625, 137.91015625, 132.91015625, 127.91015625, 123.91015625, 121.91015625, 121.91015625, 124.91015625, 129.91015625, 136.91015625, 143.91015625, 151.91015625, 158.91015625, 167.91015625, 175.91015625, 184.91015625, 193.91015625, 203.91015625, 213.91015625, 223.91015625, 238.91015625, 247.91015625, 256.91015625, 265.91015625, 274.91015625, 283.91015625, 294.91015625, 304.91015625, 315.91015625, 326.91015625, 336.91015625, 347.91015625, 357.91015625, 372.91015625, 381.91015625, 385.91015625, 393.91015625, 398.91015625, 403.91015625, 408.91015625, 412.91015625, 416.91015625, 419.91015625, 422.91015625, 423.91015625, 425.91015625, 426.91015625, 428.91015625, 428.91015625, 428.91015625, 428.91015625, 428.91015625, 428.91015625, 424.91015625, 422.91015625, 418.91015625, 414.91015625, 409.91015625, 403.91015625, 396.91015625, 386.91015625, 378.91015625, 367.91015625, 356.91015625, 346.91015625, 336.91015625, 327.91015625, 318.91015625, 309.91015625, 297.91015625, 286.91015625, 272.91015625, 259.91015625, 250.91015625, 231.91015625, 223.91015625, 217.91015625, 210.91015625, 202.91015625, 197.91015625, 192.91015625, 184.91015625, 180.91015625, 177.91015625, 173.91015625, 171.91015625, 168.91015625, 165.91015625, 163.91015625, 159.91015625, 156.91015625, 153.91015625, 150.91015625, 148.91015625, 146.91015625, 145.91015625, 144.91015625, 143.91015625, 141.91015625, 136.91015625, 130.91015625, 127.91015625, 123.91015625, 122.91015625, 122.91015625, 122.91015625], [276.91015625, 276.91015625, 276.91015625, 274.91015625, 273.91015625, 270.91015625, 266.91015625, 262.91015625, 258.91015625, 254.91015625, 249.91015625, 243.91015625, 238.91015625, 233.91015625, 226.91015625, 222.91015625, 219.91015625, 216.91015625, 213.91015625, 212.91015625, 210.91015625, 209.91015625, 209.91015625, 208.91015625, 208.91015625, 208.91015625, 209.91015625, 212.91015625, 217.91015625, 220.91015625, 223.91015625, 226.91015625, 229.91015625, 231.91015625, 232.91015625, 233.91015625, 233.91015625, 233.91015625, 233.91015625, 233.91015625, 231.91015625, 228.91015625, 223.91015625, 219.91015625, 217.91015625, 213.91015625, 210.91015625, 207.91015625, 206.91015625, 206.91015625, 206.91015625, 206.91015625, 206.91015625, 206.91015625, 208.91015625, 212.91015625, 214.91015625, 218.91015625, 222.91015625, 226.91015625, 230.91015625, 234.91015625, 238.91015625, 241.91015625, 244.91015625, 246.91015625, 249.91015625, 252.91015625, 255.91015625, 261.91015625, 264.91015625, 266.91015625, 267.91015625, 268.91015625, 268.91015625, 269.91015625, 269.91015625, 269.91015625], [269.91015625, 269.91015625, 269.91015625, 266.91015625, 262.91015625, 256.91015625, 249.91015625, 244.91015625, 239.91015625, 234.91015625, 230.91015625, 227.91015625, 224.91015625, 222.91015625, 220.91015625, 218.91015625, 216.91015625, 215.91015625, 215.91015625, 213.91015625, 213.91015625, 212.91015625, 211.91015625, 211.91015625, 211.91015625, 211.91015625, 213.91015625, 215.91015625, 220.91015625, 223.91015625, 226.91015625, 228.91015625, 231.91015625, 233.91015625, 235.91015625, 236.91015625, 236.91015625, 237.91015625, 236.91015625, 235.91015625, 230.91015625, 226.91015625, 223.91015625, 221.91015625, 219.91015625, 218.91015625, 218.91015625, 218.91015625, 218.91015625, 218.91015625, 219.91015625, 220.91015625, 221.91015625, 224.91015625, 226.91015625, 228.91015625, 231.91015625, 234.91015625, 237.91015625, 241.91015625, 245.91015625, 248.91015625, 250.91015625, 252.91015625, 253.91015625, 254.91015625, 255.91015625, 257.91015625, 260.91015625, 261.91015625, 263.91015625, 264.91015625, 265.91015625, 266.91015625, 267.91015625, 268.91015625, 268.91015625, 268.91015625, 269.91015625], [308.91015625, 308.91015625, 308.91015625, 308.91015625, 308.91015625, 308.91015625, 308.91015625, 308.91015625, 308.91015625, 308.91015625, 308.91015625, 308.91015625, 308.91015625, 310.91015625, 311.91015625, 312.91015625, 313.91015625, 315.91015625, 317.91015625, 318.91015625, 321.91015625, 324.91015625, 328.91015625, 334.91015625, 342.91015625, 349.91015625, 363.91015625, 371.91015625, 377.91015625, 384.91015625, 390.91015625, 394.91015625, 397.91015625, 400.91015625, 401.91015625, 402.91015625, 404.91015625, 404.91015625, 404.91015625, 404.91015625, 402.91015625, 397.91015625, 393.91015625, 389.91015625, 382.91015625, 379.91015625, 374.91015625, 369.91015625, 365.91015625, 362.91015625, 358.91015625, 354.91015625, 350.91015625, 346.91015625, 337.91015625, 331.91015625, 325.91015625, 321.91015625, 316.91015625, 313.91015625, 310.91015625, 307.91015625, 307.91015625]], 't': [[1589244880843, 1589244880854, 1589244881059, 1589244881071, 1589244881089, 1589244881106, 1589244881122, 1589244881139, 1589244881154, 1589244881171, 1589244881188, 1589244881204, 1589244881221, 1589244881238, 1589244881254, 1589244881271, 1589244881289, 1589244881305, 1589244881321, 1589244881337, 1589244881354, 1589244881371, 1589244881390, 1589244881404, 1589244881421, 1589244881439, 1589244881455, 1589244881472, 1589244881488, 1589244881505, 1589244881522, 1589244881538, 1589244881555, 1589244881572, 1589244881588, 1589244881604, 1589244881621, 1589244881638, 1589244881655, 1589244881671, 1589244881688, 1589244881706, 1589244881722, 1589244881739, 1589244881755, 1589244881772, 1589244881788, 1589244881805, 1589244881822, 1589244881838, 1589244881855, 1589244881872, 1589244881888, 1589244881905, 1589244881923, 1589244881938, 1589244881955, 1589244881972, 1589244881989, 1589244882006, 1589244882023, 1589244882039, 1589244882055, 1589244882071, 1589244882088, 1589244882105, 1589244882122, 1589244882138, 1589244882155, 1589244882173, 1589244882188, 1589244882205, 1589244882223, 1589244882238, 1589244882256, 1589244882272, 1589244882288, 1589244882305, 1589244882322, 1589244882338, 1589244882355, 1589244882373, 1589244882389, 1589244882405, 1589244882422, 1589244882438, 1589244882456, 1589244882472, 1589244882489, 1589244882505, 1589244882522, 1589244882538, 1589244882555, 1589244882573, 1589244882588, 1589244882605, 1589244882623, 1589244882639, 1589244882655, 1589244882672, 1589244882688, 1589244882706, 1589244882722, 1589244882738, 1589244882755, 1589244882771, 1589244882788, 1589244882806, 1589244882822, 1589244882839], [1589244883627, 1589244883640, 1589244883769, 1589244883776, 1589244883789, 1589244883812, 1589244883828, 1589244883845, 1589244883861, 1589244883879, 1589244883896, 1589244883913, 1589244883929, 1589244883945, 1589244883961, 1589244883979, 1589244883996, 1589244884011, 1589244884028, 1589244884044, 1589244884061, 1589244884078, 1589244884095, 1589244884114, 1589244884130, 1589244884145, 1589244884162, 1589244884179, 1589244884195, 1589244884211, 1589244884229, 1589244884245, 1589244884262, 1589244884279, 1589244884295, 1589244884311, 1589244884330, 1589244884346, 1589244884362, 1589244884378, 1589244884396, 1589244884416, 1589244884428, 1589244884446, 1589244884463, 1589244884479, 1589244884496, 1589244884512, 1589244884529, 1589244884545, 1589244884564, 1589244884579, 1589244884596, 1589244884615, 1589244884628, 1589244884648, 1589244884661, 1589244884679, 1589244884695, 1589244884712, 1589244884729, 1589244884746, 1589244884762, 1589244884779, 1589244884795, 1589244884813, 1589244884829, 1589244884845, 1589244884862, 1589244884879, 1589244884895, 1589244884913, 1589244884929, 1589244884946, 1589244884962, 1589244884979, 1589244884996, 1589244885015], [1589244885752, 1589244885752, 1589244885896, 1589244885913, 1589244885929, 1589244885946, 1589244885964, 1589244885980, 1589244885997, 1589244886013, 1589244886032, 1589244886047, 1589244886063, 1589244886079, 1589244886096, 1589244886113, 1589244886129, 1589244886146, 1589244886163, 1589244886179, 1589244886196, 1589244886213, 1589244886229, 1589244886246, 1589244886262, 1589244886280, 1589244886296, 1589244886313, 1589244886329, 1589244886347, 1589244886363, 1589244886379, 1589244886396, 1589244886416, 1589244886429, 1589244886446, 1589244886463, 1589244886482, 1589244886531, 1589244886546, 1589244886563, 1589244886581, 1589244886596, 1589244886614, 1589244886630, 1589244886647, 1589244886663, 1589244886679, 1589244886699, 1589244886715, 1589244886729, 1589244886746, 1589244886765, 1589244886780, 1589244886795, 1589244886813, 1589244886830, 1589244886846, 1589244886862, 1589244886880, 1589244886897, 1589244886914, 1589244886932, 1589244886947, 1589244886963, 1589244886980, 1589244886996, 1589244887013, 1589244887030, 1589244887047, 1589244887063, 1589244887080, 1589244887096, 1589244887117, 1589244887130, 1589244887148, 1589244887163, 1589244887180, 1589244887196], [1589244888293, 1589244888404, 1589244888413, 1589244888431, 1589244888447, 1589244888463, 1589244888480, 1589244888497, 1589244888517, 1589244888531, 1589244888547, 1589244888565, 1589244888580, 1589244888598, 1589244888614, 1589244888631, 1589244888647, 1589244888665, 1589244888680, 1589244888697, 1589244888714, 1589244888730, 1589244888748, 1589244888764, 1589244888781, 1589244888797, 1589244888814, 1589244888831, 1589244888847, 1589244888863, 1589244888881, 1589244888898, 1589244888914, 1589244888931, 1589244888948, 1589244888966, 1589244888981, 1589244888997, 1589244889014, 1589244889030, 1589244889046, 1589244889065, 1589244889082, 1589244889097, 1589244889114, 1589244889131, 1589244889148, 1589244889164, 1589244889181, 1589244889197, 1589244889215, 1589244889231, 1589244889248, 1589244889264, 1589244889281, 1589244889298, 1589244889314, 1589244889331, 1589244889348, 1589244889365, 1589244889381, 1589244889397, 1589244889414]]}
    # strk = Stroke(x=cs['x'], y=cs['y'], t=cs['t'])
    strks = [Stroke(x=cs['x'][i], y=cs['y'][i], t=cs['t'][i]) for i in range(len(cs['x']))]
    # clean_segment_indices, segtypes = segment_stroke(strks)
    best_match = classify_stroke(strks, templates)

    print(f"{bcolors.BOLD}", "STROKE NUMBER:", strokeNumber, f"{bcolors.ENDC}")
    print(f"{bcolors.BOLD}", "STROKE CLASS:", stroke_names[strokeNumber], f"{bcolors.ENDC}")
    if best_match == stroke_names[strokeNumber]:
        print(f"{bcolors.BOLD}", "YOUR CLASSIFICATION:", f"{bcolors.OKGREEN}", best_match, f"{bcolors.ENDC}", f"{bcolors.ENDC}")
    else:
        print(f"{bcolors.BOLD}", "YOUR CLASSIFICATION:", f"{bcolors.FAIL}", best_match, f"{bcolors.ENDC}", f"{bcolors.ENDC}")

    plot_segmentation(strks, clean_segment_indices, segtypes)
    plt.figure(1).canvas.set_window_title('MIT 6.835: Stroke Segmentation')
    plt.show()
else:
    msg = 'Stroke index out of range. Give a number between 1 and ' + str(strokes.size)
    raise ValueError(msg)
