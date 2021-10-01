

list_actions = [
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



"""transformation du tableau des actions en binaire"""

n = len(list_actions)
integer_list = [i for i in range(2**n)]

binaire_list = [bin(i)[2:] for i in integer_list]

all_combinaisons = ["0"*(n-len(k)) + k for k in binaire_list]





celling = 500
valid_combinations = []

for combi in all_combinaisons:
    cost_combi = 0
    benefit_combi = 0
    for i in range(n):
        if combi[i] == "1":
            cost_combi = cost_combi + list_actions[i]["cost"]
            benefit_combi = benefit_combi + (list_actions[i]["cost"] * list_actions[i]["benefit"])

    if cost_combi <= celling:
        valid_combinations.append([combi, cost_combi, benefit_combi])


best_investment = valid_combinations[0][0]
best_cost = valid_combinations[0][1]
best_benefit = valid_combinations[0][2]
for combi in valid_combinations:
    if combi[1] > best_benefit:
        best_investment = combi[0]
        best_cost = combi[1]
        best_benefit = combi[2]

list_op = []
for i in range(len(best_investment)):
    if best_investment[i] == "1":
        list_op.append(list_actions[i]["name"])


print(list_op)
































    
   





    




















