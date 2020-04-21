from Template import Template

template_data = [
    {
        'name': 'HEART',
        'x': [0.4182692307692308, 0.0, 0.0673076923076923, 0.46634615384615385, 0.6057692307692307, 1.0, 0.9903846153846154, 0.7836538461538461, 0.40865384615384615],
        'y': [0.9915611814345991, 0.7046413502109705, 0.016877637130801686, 0.16455696202531644, 0.03375527426160337, 0.0, 0.2869198312236287, 0.6919831223628692, 1.0]
    },
    {
        'name': 'HEART',
        'x': [0.4575645756457565, 0.08118081180811808, 0.0, 0.36162361623616235, 0.4870848708487085, 0.7416974169741697, 1.0, 0.6273062730627307, 0.44649446494464945],
        'y': [0.9775784753363229, 0.5605381165919282, 0.12556053811659193, 0.026905829596412557, 0.3811659192825112, 0.0, 0.18385650224215247, 0.8609865470852018, 1.0]
    },
    {
        'name': 'PARTY',
        'x': [0.4398826979472141, 0.0, 0.7272727272727273, 0.4398826979472141, 0.5278592375366569, 0.6627565982404692, 0.7917888563049853, 0.7917888563049853, 0.6627565982404692, 0.9296187683284457, 0.9560117302052786, 1.0],
        'y': [0.24193548387096775, 1.0, 0.7701612903225806, 0.3185483870967742, 0.0, 0.3024193548387097, 0.27419354838709675, 0.27419354838709675, 0.5645161290322581, 0.5645161290322581, 0.8104838709677419, 0.8064516129032258]
    },
    {
        'name': 'SMILE',
        'x': [0.6860986547085202, 0.06278026905829596, 1.0, 0.8789237668161435, 0.7040358744394619, 0.1210762331838565, 0.0, 0.0, 0.3273542600896861, 0.4439461883408072],
        'y': [0.0, 1.0, 0.5607843137254902, 0.2196078431372549, 0.06274509803921569, 0.38823529411764707, 0.6196078431372549, 0.6235294117647059, 0.6901960784313725, 0.48627450980392156]
    },
     {
        'name': 'THUMBSUP',
        'x': [0.018518518518518517, 0.49074074074074076, 0.4351851851851852, 0.6944444444444444, 0.5648148148148148, 0.9675925925925926, 1.0, 0.0],
        'y': [0.4749034749034749, 0.13513513513513514, 0.0, 0.0888030888030888, 0.47104247104247104, 0.6254826254826255, 1.0, 0.44787644787644787]
    },
     {
        'name': 'FIRE',
        'x': [0.2809917355371901, 0.5619834710743802, 0.8016528925619835, 0.9669421487603306, 1.0, 0.0, 0.256198347107438],
        'y': [0.3918918918918919, 0.0, 0.36486486486486486, 0.36936936936936937, 0.6711711711711712, 1.0, 0.4099099099099099]
    },
     {
        'name': 'FIRE',
        'x': [0.10037174721189591, 0.3828996282527881, 0.7843866171003717, 1.0, 0.9330855018587361, 0.8550185873605948, 0.7063197026022305, 0.6356877323420075, 0.5539033457249071, 0.45353159851301117, 0.2899628252788104, 0.1821561338289963, 0.0037174721189591076, 0.0, 0.23048327137546468],
        'y': [0.906158357771261, 1.0, 0.9120234604105572, 0.656891495601173, 0.18181818181818182, 0.2932551319648094, 0.41935483870967744, 0.12023460410557185, 0.0, 0.03225806451612903, 0.4252199413489736, 0.18475073313782991, 0.12316715542521994, 0.8709677419354839, 0.9648093841642229]
    },
    { 'name': 'PRAY',
    'x': [0.6398891966759003, 0.5734072022160664, 0.4626038781163435, 0.46814404432132967, 0.2742382271468144, 0.0, 0.4293628808864266, 1.0],
    'y': [0.7222222222222222, 0.0, 0.13271604938271606, 0.5216049382716049, 0.6234567901234568, 1.0, 0.8271604938271605, 0.7839506172839507]
    },
    {'name': 'HEARTEYES',
    'x': [0.8938053097345132, 0.1415929203539823, 1.0, 0.7699115044247787, 0.1504424778761062, 0.0],
    'y': [0.0, 0.5777777777777777, 0.7166666666666667, 0.5444444444444444, 1.0, 0.9722222222222222]
    },
    {
    'name': 'CRYING',
    'x': [0.5336538461538461, 1.0, 0.04807692307692308, 0.5625, 0.0, 0.12980769230769232, 0.19230769230769232, 0.32211538461538464, 0.42788461538461536, 0.4855769230769231],
    'y': [0.0, 0.5, 0.38686131386861317, 0.40875912408759124, 0.6496350364963503, 1.0, 0.8868613138686131, 0.7956204379562044, 0.8759124087591241, 0.9598540145985401]
    },
        {
    'name': 'CHECKMARK',
    'x': [0.0, 0.17592592592592593, 1.0],
    'y': [0.6153846153846154, 1.0, 0.0]
    },
        {
    'name': 'SOCCERBALL',
    'x': [0.5198237885462555, 1.0, 0.2511013215859031, 0.0, 0.2422907488986784, 0.1894273127753304, 0.6960352422907489, 0.762114537444934, 0.4185022026431718, 0.5594713656387665, 0.9074889867841409, 0.7709251101321586, 0.9647577092511013],
    'y': [0.0, 0.2988505747126437, 0.367816091954023, 0.5632183908045977, 0.6130268199233716, 1.0, 0.7432950191570882, 0.7701149425287356, 0.47509578544061304, 0.578544061302682, 0.24521072796934865, 0.23754789272030652, 0.6398467432950191]
    },
    {
    'name': 'BREAD',
    'x': [0.8408163265306122, 0.1510204081632653, 0.0, 0.5306122448979592, 1.0, 0.9591836734693877, 0.8122448979591836],
    'y': [0.0, 0.6445182724252492, 1.0, 0.7342192691029901, 0.11295681063122924, 0.0033222591362126247, 0.03322259136212625]
    },
    # {
    # 'name': 'SOCCERBALL',
    # 'x': [0.5198237885462555, 1.0, 0.2511013215859031, 0.0, 0.2422907488986784, 0.1894273127753304, 0.6960352422907489, 0.762114537444934, 0.4185022026431718, 0.5594713656387665, 0.9074889867841409, 0.7709251101321586, 0.9647577092511013],
    # 'y': [0.0, 0.2988505747126437, 0.367816091954023, 0.5632183908045977, 0.6130268199233716, 1.0, 0.7432950191570882, 0.7701149425287356, 0.47509578544061304, 0.578544061302682, 0.24521072796934865, 0.23754789272030652, 0.6398467432950191]
    # },
    # {
    #     'name': 'TRIANGLE',
    #     'x':  [0.002264754207558062, 0.468448865402549, 0.7969270393889605, 0.9660730938318753, 0.9907633553887828, 0.16896842666192993, 0.001731870864603224] ,
    #     'y':  [0.1607008760951189, 0.6712140175219024, 1.0, 0.3127659574468085, 0.0036795994993742177, 0.13732165206508135, 0.14966207759699623]
    # },
    # {
    #     'name': 'CURVE',
    #     'x':  [0.0001170583243100875, 0.28009130549296185, 0.8449269848702116, 0.8989786661203945, 0.01714904451142782, 1.0] ,
    #     'y':  [1.0, 0.1180457859061261, 0.4634224325361299, 0.5738585496866607, 0.8530502621818646, 0.6871722726691393]
    # },
    # {
    #     'name': 'CHEF HAT',
    #     'x':  [0.7797098601696303, 0.7868159937125454, 0.7844581982513017, 0.8026656187575728, 0.7858335789370272, 0.998886596587746, 0.7840324851819105, 0.43484952680354977, 0.46209516324458855, 0.7841634738186463, 0.0, 0.7868159937125454, 0.215705537544618, 0.7861283033696826, 0.24530896944690048, 0.24864917968366243] ,
    #     'y':  [0.0, 0.09080116975996758, 0.25115093957205314, 0.406723224368069, 0.05605582418855141, 0.6362451863219156, 0.27639922402061556, 0.5229464053044561, 0.7321423400990242, 0.2634276283406202, 0.6600167935836928, 0.08309928482497032, 0.4685120305759041, 0.06474216058140544, 0.16113154008744246, 0.07490517416104468]
    # },
    # {
    #     'name': 'SKEWED CIRCLE',
    #     'x':  [0.41228845461389896, 0.78942027562277, 1.0, 0.78942027562277, 0.335821139808177, 0.20612786015908868, 0.11496284657435596, 0.04239091295950768, 0.0, 0.5636518380307047, 0.35405414252512357, 0.5204425676781564] ,
    #     'y':  [0.027030173216613895, 0.12101881169677779, 0.51964984168374, 0.12101881169677779, 0.9644021233004284, 0.8909713168187744, 0.8026634382566586, 0.6821801080275657, 0.47008288321847647, 0.031104488731607375, 0.01951015086608307, 0.0]
    # },
    # {
    #     'name': 'OMEGA',
    #     'x':  [1.0, 0.5966863975728011, 0.858294416847616, 0.8512150867069217, 0.6758975579285523, 0.13352568488057348, 0.17796484130997353, 0.3651804039382492, 0.008596329456557304] ,
    #     'y':  [0.016814401900758474, 0.004523439641780133, 0.008407200950379237, 0.4960477017271315, 0.002444485058941789, 0.6846385817417527, 0.4297039203143562, 0.0214749154710774, 0.031435620944896284]
    # },
    # {
    #     'name': 'STRAIGHT LINE',
    #     'x':  [0.0, 1.0] ,
    #     'y':  [1.0, 0.0]
    # },
    # {
    #     'name': 'MUSIC NOTE',
    #     'x':  [1.0, 0.48480072055843276, 0.5983787435262329, 0.7429407791038054, 0.0017113262778653457, 0.7630263454176988, 0.46813780680027023, 0.5151992794415672] ,
    #     'y':  [0.7482053751203712, 1.0, 0.03952551869036155, 0.8599754880504246, 0.23209752254223934, 0.8509148209752254, 0.35489801278123084, 0.2841416440514751]
    # },
    # {
    #     'name': 'SIGMA',
    #     'x':  [0.0, 0.9956450734893849, 0.06759742546991579, 0.9300970252009351, 0.08447276569854943] ,
    #     'y':  [0.0, 0.2845891685998224, 0.5258756479651746, 0.8346077841738981, 0.9970787868373572]
    # },
    # {
    #     'name': 'DOME',
    #     'x':  [1.0, 0.9940028350234434, 0.9865881583251553, 0.9909133863991567, 0.9282520990077417, 0.9371933267909716, 0.016355904481517827, 0.9310144295423981, 0.8581761349180388] ,
    #     'y':  [0.9994583405877004, 0.9944093010659083, 0.9346139709438416, 0.7833555800591956, 0.0973632793608419, 0.030661791731955972, 0.0005416594122995376, 0.061652448107093805, 0.11312943725456058]
    # },
    # {
    #     'name': 'THREE FEATHERS',
    #     'x':  [0.9296620082497076, 0.9933201994705412, 0.9915040325063104, 0.9915040325063104, 0.6592070430339223, 0.6823554762051345, 0.7599889183032691, 0.6692729175644894, 0.7932032260050483, 0.5326910053561534, 0.9891337807055347, 0.000523302345625808, 0.9683555993350982, 0.047589730961029364, 0.20079418826571446, 0.2948962630056024, 0.3953087483839192] ,
    #     'y':  [0.07474268470119093, 0.28207684431750824, 0.556205205582799, 0.556205205582799, 0.6935118823085628, 0.5009969283828205, 0.1742199709004688, 0.3894756695586571, 0.9859621706094736, 0.16535539149647033, 0.5957320687611144, 0.14827288893678936, 0.17513606725224984, 0.04362235275098346, 0.004418817696825996, 0.0, 0.033706956943471464]
    # },
    # {
    #     'name': 'TWO MOUNTAINS',
    #     'x':  [0.0016486180701470825, 0.15467916599321158, 0.18600290932600613, 0.31200905123646355, 0.4491352836592856, 0.7243575238403104, 0.7743332794569258, 0.9994504606432844, 0.020300630353967997] ,
    #     'y':  [0.1754149627134953, 0.7920134712533077, 0.9591291796968968, 0.5988693769545346, 0.1465479913399086, 0.8874909790714458, 1.0, 0.0656483040654318, 0.018787587202309358]
    # },
    # {
    #     'name': 'FIVE',
    #     'x':  [0.0, 0.9604369018393994, 0.9995374817661081, 0.43871633400932153, 0.11737289643149393, 0.3260397765681147, 0.9421496424378268] ,
    #     'y':  [0.9987034984630183, 0.9347776081637774, 0.5848894836996299, 0.9743209050417181, 0.26664017900085735, 0.979757846970996, 0.16990443528993537]
    # }
]

def get_templates():
    templates = []
    for tm in template_data:
        temp = Template(name = tm['name'],x=tm['x'], y=tm['y'])
        templates.append(temp)
    return templates
