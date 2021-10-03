#! /user/bin/env python3
# -*- coding: utf-8 -*-
import csv

CELLING = 500


def file_conversion_to_dict(file):
    reader = csv.DictReader(open(file, "r"), delimiter=";")
    return [dict(line) for line in reader]


def get_all_combination(dict_actions):
    """

    :param dict_actions:
    :return:
    """
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


def get_best_investment(tab):

    best_investment = tab[0][0]
    best_investment_cost = tab[0][1]
    best_investment_benefit = tab[0][2]
    for investment in tab:
        if investment[2] > best_investment_benefit:
            best_investment = investment[0]
            best_investment_cost = investment[1]
            best_investment_benefit = investment[2]

    return [best_investment, best_investment_cost, best_investment_benefit]


def format_best_investment(investment, tab):
    best_actions_list = []
    action_name = investment[0]
    for i in range(len(action_name)):
        if action_name[i] == "1":
            best_actions_list.append(tab[i]["name"])

    print("Best investment : actions: {}, Cost : {}€,  Benefit : {}€ ".format(best_actions_list, investment[1],
                                                                              round(investment[2], 2)))


def main():
    tab_actions = file_conversion_to_dict("action_list.csv")
    tab_investments = get_all_combination(tab_actions)
    valid_investments = get_valid_investment(tab_investments, tab_actions)
    best_investment = get_best_investment(valid_investments)
    format_best_investment(best_investment, tab_actions)


if __name__ == "__main__":
    main()
