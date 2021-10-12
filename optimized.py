#! /user/bin/env python3
# -*- coding: utf-8 -*-


import csv

CELLING = 500


def convert_file_to_dict(file):
    reader = csv.DictReader(open(file, "r"))
    return [dict(line) for line in reader]


def action_profit(tab):
    action_list = []
    for action in tab:
        if int(float(action["price"])) > 0:
            action["benefit"] = abs(int(float(action["price"]))) * int(float(action["profit"]))/100
            action_list.append(action)
    return action_list


def format_output(profit, tab):
    print("Best investment :")
    cost = 0
    for action in tab:
        cost += int(float(action["price"]))
        print(action["name"] + " " + str(action["price"]) + "€")

    print()
    print("Total cost : {}€".format(cost))
    print("Profit : {}€".format(profit))


def get_best_investment(celling, tab):

    tab_matrix = [[0 for x in range(celling + 1)] for x in range(len(tab) + 1)]

    for i in range(1, len(tab) + 1):
        for price in range(1, celling + 1):
            if int(float(tab[i-1]["price"])) <= price:
                tab_matrix[i][price] = max(tab[i - 1]["benefit"]
                                           + tab_matrix[i-1][price-(int(float(tab[i-1]["price"])))],
                                           tab_matrix[i-1][price])
            else:
                tab_matrix[i][price] = tab_matrix[i-1][price]

    w = celling
    n = len(tab)
    best_investment = []

    while w >= 0 and n >= 0:
        action = tab[n-1]
        if tab_matrix[n][w] == tab_matrix[n-1][w-(int(float(action["price"])))] + action["benefit"]:
            best_investment.append(action)
            w -= int(float(action["price"]))

        n -= 1

    return format_output(round(tab_matrix[-1][-1], 2), best_investment)


def main():
    print("Welcome to AlgoInvest&Trade")
    tab_actions = convert_file_to_dict("dataset2_Python+P7.csv")
    tab_benefit = action_profit(tab_actions)
    get_best_investment(CELLING, tab_benefit)


if __name__ == "__main__":
    main()
