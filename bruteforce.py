#! /user/bin/env python3
# -*- coding: utf-8 -*-
import csv

CELLING = 500


def file_conversion_to_dict(file):
    reader = csv.DictReader(open(file, "r"), delimiter=";")
    return [dict(line) for line in reader]


def dict_conversion_to_bin(dict_actions):
    n = len(dict_actions)
    tab_integer = [i for i in range(2**n)]
    tab_bin = [bin(i)[2:] for i in tab_integer]
    return ["0"*(n-len(k)) + k for k in tab_bin]


def get_valid_investment(tab1, tab2):
    valid_investment = []
    for investment in tab1:
        cost_investment = 0
        benefit_investment = 0
        for i in range(len(tab2)):
            if investment[i] == "1":
                cost_investment += int(tab2[i]["cost"])
                benefit_investment += int(tab2[i]["cost"]) * (int(tab2[i]["benefit"]) / 100)

        if cost_investment <= CELLING:
            valid_investment.append([investment, cost_investment, benefit_investment])
    return valid_investment


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


def format_best_investment(investment, tab):
    best_actions_list = []
    best_action_name = investment[0]
    for i in range(len(best_action_name)):
        if best_action_name[i] == "1":
            best_actions_list.append(tab[i]["name"])

    print("Best investment : actions: {}, Cost : {}€,  Benefit : {}€ ".format(best_actions_list, investment[1],
                                                                              round(investment[2], 2)))


def main():
    tab_actions = file_conversion_to_dict("action_list.csv")
    print(tab_actions)


    """
    tab_investments = dict_conversion_to_bin(tab_actions)
    valid_investments = get_valid_investment(tab_investments, tab_actions)
    best_investment = tri_fusion(valid_investments, 0, len(valid_investments) - 1)[-1]
    format_best_investment(best_investment, tab_actions)
    """


if __name__ == "__main__":
    main()
