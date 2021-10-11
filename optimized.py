#! /user/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter
import csv


def convert_file_to_dict(file):
    reader = csv.DictReader(open(file, "r"))
    return [dict(line) for line in reader]


def action_profit(tab):
    action_list = []
    for action in tab:
        action["benefit"] = int(action["price"]) * int(action["profit"])/100
        action_list.append(action)
    return action_list


def get_best_investment(tab, celling):
    tab_sorted = sorted(tab, key=itemgetter("benefit"), reverse=True)
    total_investment = 0
    best_investment = []

    i = 0
    while i < len(tab) and total_investment < celling:
        action = tab_sorted[i]
        price_action = tab_sorted[i]["price"]
        if total_investment + int(price_action) <= celling:
            best_investment.append(action)
            total_investment += int(price_action)
        i = i + 1

    return best_investment


def format_output(tab):
    cost = 0
    actions_list =[]
    profit = 0
    for action in tab:
        cost += int(action["price"])
        profit += action["benefit"]
        print(action["name"] + " " + action["price"])

    print()
    print("Total cost : {}€".format(cost))
    print("Profit : {}€".format(round(profit, 2)))


def main():
    print("Welcome to AlgoInvest&Trade")
    tab_actions = convert_file_to_dict("actions_list.csv")
    tab_benefit = action_profit(tab_actions)
    best_investment = get_best_investment(tab_benefit, 500)
    format_output(best_investment)


if __name__ == "__main__":
    main()




