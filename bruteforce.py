

tab_actions = [
    {"name": "action-1",
     "cost": 20,
     "benefit": 0.05},

    {"name": "action-2",
     "cost": 30,
     "benefit": 0.10},

    {"name": "action-3",
     "cost": 50,
     "benefit": 0.15},

    {"name": "action-4",
     "cost": 70,
     "benefit": 0.20},

    {"name": "action-5",
     "cost": 60,
     "benefit": 0.17},

    {"name": "action-6",
     "cost": 80,
     "benefit": 0.25},

    {"name": "action-7",
     "cost": 22,
     "benefit": 0.07},

    {"name": "action-8",
     "cost": 26,
     "benefit": 0.11},

    {"name": "action-9",
     "cost": 48,
     "benefit": 0.13},

    {"name": "action-10",
     "cost": 34,
     "benefit": 0.27},

    {"name": "action-11",
     "cost": 42,
     "benefit": 0.17},

    {"name": "action-12",
     "cost": 110,
     "benefit": 0.09},

    {"name": "action-13",
     "cost": 38,
     "benefit": 0.23},

    {"name": "action-14",
     "cost": 14,
     "benefit": 0.01},

    {"name": "action-15",
     "cost": 18,
     "benefit": 0.03},

    {"name": "action-16",
     "cost": 8,
     "benefit": 0.08},

    {"name": "action-17",
     "cost": 4,
     "benefit": 0.12},

    {"name": "action-18",
     "cost": 10,
     "benefit": 0.14},

    {"name": "action-19",
     "cost": 24,
     "benefit": 0.21},

    {"name": "action-20",
     "cost": 114,
     "benefit": 0.18},
]




"""
1- trouver toutes les possibilités d'investissement 

  un budget de 500
2 - parmis toutes les possibilités évaluer celle qui offres 
"""

"""transformation du tableau des actions en binaire

n = len(tab_actions)
tab_integer = [i for i in range(2**n)]

tab_bin = [bin(i)[2:] for i in tab_integer]

tab_combinaisons = ["0"*(n-len(k)) + k for k in tab_bin]


celling = 500
valid_combinations = []

for combinaison in tab_combinaisons:
    cost_combinaison = 0
    benefit_combinaison = 0
    for i in range(n):
        if combinaison[i] == "1":
            cost_combinaison = cost_combinaison + tab_actions[i]["cost"]
            benefit_combinaison = benefit_combinaison + (tab_actions[i]["cost"] * tab_actions[i]["benefit"])

    if cost_combinaison <= celling:
        valid_combinations.append([combinaison, cost_combinaison, benefit_combinaison])
print(valid_combinations[10:])

"""


def fusion(tab_1, tab_2):
    tab_fusion = []
    i = 0
    j = 0
    while i < len(tab_1) and j < len(tab_2):
        combi1 = tab_1[i]
        benefit_combi1 = tab_1[i][2]
        combi2 = tab_2[j]
        benefit_combi2 = tab_2[i][2]
        if benefit_combi1 <= benefit_combi2:
            tab_fusion.append(combi1)
            i = i + 1
        else:
            tab_fusion.append(combi2)
            j = j + 1
        if i == len(tab_1):
            while j < len(tab_2):
                tab_fusion.append(tab_2[j])
                j = j + 1
        elif j == len(tab_2):
            while i < len(tab_1):
                tab_fusion.append(tab_1[i])
                i = i + 1

    return tab_fusion


tab1 = [['11111111110010001100', 492, 86.14000000000001],
         ['11111111110010010000', 486, 84.9],
         ['11111111110010010100', 496, 86.30000000000001],
         ['11111111110010011000', 490, 85.38000000000001],
         ['11111111110010011100', 500, 86.78000000000002]]

tab2 = [['11111111110010101000', 500, 85.28000000000002],
        ['11111111110011000000', 492, 84.4],
        ['11111111110011001000', 496, 84.88000000000001],
        ['11111111110011010000', 500, 85.04],
        ['11111111111000000000', 482, 82.66000000000001],
        ['11111111111000000100', 492, 84.06000000000002],
        ['11111111111000001000', 486, 83.14000000000001],
        ['11111111111000001100', 496, 84.54000000000002],
        ['11111111111000010000', 490, 83.30000000000001]]


tab = fusion(tab1, tab2)
print(tab)
































    
   





    




















