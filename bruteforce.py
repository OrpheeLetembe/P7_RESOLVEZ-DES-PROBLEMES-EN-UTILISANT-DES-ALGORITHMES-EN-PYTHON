#! /user/bin/env python3
# -*- coding: utf-8 -*-
import csv

CELLING = 500


def convert_file_to_dict(file):
    reader = csv.DictReader(open(file, "r"))
    return [dict(line) for line in reader]


def get_all_combination(dict_actions):
    """ This function converts the list of dictionaries passed as parameters into a list of integers
    and returns the set of possible investment combinations as a binary list.

    :param dict_actions: Dictionary list with the name of the action, its price and its benefit as keys.
    :return list: All possible combinations in the form of a binary.
    """
    n = len(dict_actions)
    tab_integer = [i for i in range(2**n)]
    tab_bin = [bin(i)[2:] for i in tab_integer]
    return ["0"*(n-len(k)) + k for k in tab_bin]


def get_valid_investment(tab1, tab2):
    """ This function calculates the cost of the investment and the profit before returning the list of investments
    whose cost is less than or equal to the ceiling.

    :param tab1:  All possible combinations.
    :param tab2: Dictionary list with the name of the action, its price and its benefit as keys.
    :return list: investment costing less than or equal to the ceiling.
    """
    valid_investment = []
    for investment in tab1:
        price_investment = 0
        profit_investment = 0
        for i in range(len(tab2)):
            if investment[i] == "1":
                price_investment += int(tab2[i]["price"])
                profit_investment += int(tab2[i]["price"]) * (int(tab2[i]["profit"]) / 100)

        if price_investment <= CELLING:
            valid_investment.append([investment, price_investment, profit_investment])
    return valid_investment


def get_best_investment(tab):
    """ This function which takes as input the list of valid investments returns the one which offers
    the maximum profit.

    :param tab: list of investments whose cost is less than or equal to the ceiling.
    :return: the action list that provides the best profit, the cost of the investment and the profit generated.
    """

    best_investment = tab[0][0]
    best_investment_price = tab[0][1]
    best_investment_profit = tab[0][2]
    for investment in tab:
        if investment[2] > best_investment_profit:
            best_investment = investment[0]
            best_investment_price = investment[1]
            best_investment_profit = investment[2]

    return [best_investment, best_investment_price, best_investment_profit]


def format_output(investment, tab):
    """

    :param investment:
    :param tab:
    
    """
    best_actions_list = []
    action_name = investment[0]
    for i in range(len(action_name)):
        if action_name[i] == "1":
            best_actions_list.append([tab[i]["name"], tab[i]["price"]])

    print("Best investment :")
    for action in best_actions_list:
        print(action[0] + "  " + action[1] + "€")
    print()
    print("Total cost : {}€".format(investment[1]))
    print("Profit : {}€".format(round(investment[2], 2)))


def main():
    print("Welcome to AlgoInvest&Trade")
    tab_actions = convert_file_to_dict("actions_list.csv")
    tab_investments = get_all_combination(tab_actions)
    valid_investments = get_valid_investment(tab_investments, tab_actions)
    best_investment = get_best_investment(valid_investments)
    format_output(best_investment, tab_actions)


if __name__ == "__main__":
    main()
