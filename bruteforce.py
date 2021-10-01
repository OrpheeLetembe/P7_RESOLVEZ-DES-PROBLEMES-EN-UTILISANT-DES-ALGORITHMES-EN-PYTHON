
import csv

lecteur = csv.DictReader(open("action_list.csv", "r"))
tab_actions = [dict(ligne) for ligne in lecteur]


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
            cost_combinaison += int(tab_actions[i]["cost"])
            benefit_combinaison += int(tab_actions[i]["cost"]) * (int(tab_actions[i]["benefit"]) / 100)

    if cost_combinaison <= celling:
        valid_combinations.append([combinaison, cost_combinaison, benefit_combinaison])


def fusion(tab_1, tab_2):
    tab_fusion = []
    i = 0
    j = 0
    while i < len(tab_1) and j < len(tab_2):
        combi1 = tab_1[i]
        benefit_combi1 = tab_1[i][2]
        combi2 = tab_2[j]
        benefit_combi2 = tab_2[j][2]
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


def tri_fusion(tab, start, end):
    if start == end:
        return [tab[start]]
    else:
        i = (end - start) // 2
        tab_part1 = tri_fusion(tab, start, start + i)
        tab_part2 = tri_fusion(tab, start + 1 + i, end)
        return fusion(tab_part1, tab_part2)


print(tri_fusion(valid_combinations, 0, len(valid_combinations) - 1))




























    
   





    




















