
import csv

reader = csv.DictReader(open("action_list.csv", "r"))
tab_actions = [dict(line) for line in reader]


n = len(tab_actions)


tab_integer = [i for i in range(2**n)]

tab_bin = [bin(i)[2:] for i in tab_integer]

tab_investments = ["0"*(n-len(k)) + k for k in tab_bin]


celling = 500
valid_investments = []

for investment in tab_investments:
    cost_investment = 0
    benefit_investment = 0
    for i in range(n):
        if investment[i] == "1":
            cost_investment += int(tab_actions[i]["cost"])
            benefit_investment += int(tab_actions[i]["cost"]) * (int(tab_actions[i]["benefit"]) / 100)

    if cost_investment <= celling:
        valid_investments.append([investment, cost_investment, benefit_investment])


def fusion(tab_1, tab_2):
    tab_fusion = []
    i = 0
    j = 0
    while i < len(tab_1) and j < len(tab_2):
        first_combination = tab_1[i]
        second_combination = tab_2[j]
        if first_combination[2] <= second_combination[2]:
            tab_fusion.append(first_combination)
            i = i + 1
        else:
            tab_fusion.append(second_combination)
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


best_investment = tri_fusion(valid_investments, 0, len(valid_investments) - 1)[-1]

best_actions_list = []
best_action_name = best_investment[0]
for i in range(len(best_action_name)):
    if best_action_name[i] == "1":
        best_actions_list.append(tab_actions[i]["name"])


print("Best investment : actions: {}, Cost : {}€,  Benefit : {}€ ".format(best_actions_list, best_investment[1],
                                                                          round(best_investment[2], 2)))
