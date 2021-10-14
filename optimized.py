#! /user/bin/env python3
# -*- coding: utf-8 -*-

import glob
import csv

CELLING = 500


def convert_file_to_dict(file):
    reader = csv.DictReader(open(file, "r"))
    return [dict(line) for line in reader]


def action_profit(tab):
    """ This function is used to add a key:value pair to each share of the list
    with key being benefit and value being the price of the share * its profit.

    :param tab: Dictionary list with the name of the action and its price as keys.
    :return list: Dictionary list with the name of the action, its price and its benefit as keys.
    """
    action_list = []
    for action in tab:
        if int(float(action["price"])) > 0:
            action["benefit"] = abs(int(float(action["price"]))) * int(float(action["profit"]))/100
            action_list.append(action)
    return action_list


def format_output(profit, tab):
    """ This function has for role to display the results of research of the best investment.

    :param profit:the profit generated by the best combination of shares
    :param tab:the share list that provides the best profit.
    """
    print()
    print("-- Best investment --")
    cost = 0
    for action in tab:
        cost += int(float(action["price"]))
        print(action["name"] + " " + str(action["price"]) + "€")

    print()
    print("Total cost : {}€".format(cost))
    print("Profit : {}€".format(profit))


def get_best_investment(celling, tab):
    """ This function is used to determine the best investment by creating and filling the matrix.

    :param celling:The investment limit.
    :param tab:Dictionary list with the name of the action, its price and its benefit as keys.
    :return:The best profit and the share list to obtain it.
    """
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


def run_algo():
    csvfiles = []
    for file in glob.glob("*.csv"):
        csvfiles.append(file)
    for k, file in enumerate(csvfiles):
        print(k + 1, file)

    choice = input("Choose the dataset to be processed : ")
    result = choice.isdigit()

    if result:
        file_choose = int(choice)

        if file_choose in range(1, len(csvfiles) + 1):
            tab_actions = convert_file_to_dict(str(csvfiles[file_choose - 1]))
            tab_benefit = action_profit(tab_actions)
            get_best_investment(CELLING, tab_benefit)

        else:
            print("You must choose a dataset from the list")
    else:
        print("You must choose a dataset from the list")


def main():
    print("--------- WELCOME TO ALGOINVEST&TRADE ----------")
    menu = True
    while menu:
        print()
        print("---- MENU ----")
        print("1 RUN ALGORITHM")
        print("2 EXIT")

        choice = input("What do you want to do : ")
        if choice == "1":
            print()
            print("--- Dataset list ---")
            run_algo()
        elif choice == "2":
            print("-------- THANK YOU FOR USING ALGOINVEST&TRADE --------")
            menu = False
        else:
            print("You must choose a menu item")


if __name__ == "__main__":
    main()
