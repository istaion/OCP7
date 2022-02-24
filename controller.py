from view import *
from model import *
from time import time
import csv
import pandas as pd


def getdonnee(file):
    """
    get the data and put it in array of Action object
    :param file: path to csv file
    :return: array of Action object
    """
    data = pd.read_csv("donnees/" + file)
    list_action = []
    for item in data.values:
        if item[1] <= 0:  # If the action have a negative price
            print("L'action :", item[0], "a un prix nul ou négatif. Elle ne sera pas prise en compte")
            pass
        else:
            list_action.append(Action(item))
    return list_action


def error_input(res, n, m):
    """
    asks for an input until it is validated
    :param res: input
    :param n: min
    :param m: max
    :return: res
    """
    res = int(res)
    while res < n or res > m:
        print("veuillez entrer un nombre entre ", n, " et ", m, ":")
        res = int(input())
    return res


def select_program(number, data, money):
    """
    run the appropriate function to use the selected program
    :param number: 1 for brutal force, 2 for dynamic programation, 3 for "glouton" algorithm
    :param data: array of actions
    :param money: money to use
    :return: a tuple with solution objet and time spend
    """
    money = float(money)
    t1 = time()
    if number == 1:
        res = brutal_force(data, money)
        return res, time()-t1
    elif number == 2:
        res = dynamic_prog(data, money)
        return res, time() - t1
    else:
        res = glouton(data, money)
        return res, time() - t1

# brutal force functions :


def brutal_force(data, money):
    """
    examine all possibility and take the best
    :param data: array of actions
    :param money: money to use
    :return: Solution object
    """
    keys = ["benefice"]
    for action in data:
        keys.append(action.name)
    with open("brutalsolutions.csv", "w") as csvfile:  # init csv with solutions
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(keys)
    counting(data, money, [])  # write all possibility in the csv file
    df = pd.read_csv("brutalsolutions.csv")  # create a pandas data
    df = df.sort_values(by="benefice", ascending=False)
    soluc = []
    for action in data:  # take the best possibility
        if action.is_in_solution(df.iloc[0]):
            soluc.append(action)
    soluc = Solution(soluc)
    return soluc


def counting(list_actions, money, res):
    """
    count all possibility, calcul profit and write it in the csv file
    :param list_actions: array of actions
    :param money: money to use
    :param res: list of tuple : action, and 1 for purchase 0 else.
    :return:
    """
    if len(list_actions) == 0:  # Calcul of the profit and add solution to csv file if all actions have been checked
        profit = 0
        for action in res:
            profit += action[0].earned * action[1]
        value = [profit]
        for action in res:
            value.append(action[1])
        with open("brutalsolutions.csv", "a") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(value)
    else:  # Select and supress the first action and recall the function
        # without purchase and with purchase (if there is enough money).
        action_selected = list_actions[0]
        newlist = list(list_actions)
        newlist.pop(0)
        res0 = list(res)
        res0.append((action_selected, 0))
        counting(newlist, money, res0)
        if money >= action_selected.price:  # if there is enough money
            res1 = list(res)
            res1.append((action_selected, 1))
            counting(newlist, money - action_selected.price, res1)

# dynamic program functions :


def dynamic_prog(data, money):
    """
    Create the tab, resolve, return the solution
    :param data: array of actions
    :param money: money to use
    :return: Solution object
    """
    money = round(float(money) * 100)
    creation_tab(data, money)
    tab = pd.read_csv("tableau_prog_dynamique.csv", header=None)  # put the csv in a pandas data
    soluc = resolution(tab, money, len(data) - 1, data, [])
    return Solution(soluc)


def creation_tab(donnee, money):
    """
    Create the table and write it in a csv file
    :param donnee: array of action
    :param money: money to use
    :return:
    """
    with open("tableau_prog_dynamique.csv", "w"):  # init csv
        pass
    for i, action in enumerate(donnee):
        newline = []  # new line to put in csv
        for n in range(money+1):
            if i == 0:  # first line init
                if n >= action.cent_price:
                    newline.append(action.cent_earned)
                else:
                    newline.append(0)
            elif n >= action.cent_price:  # select the best : purchase or not
                newline.append(max(lastline[n], lastline[n-action.cent_price]+action.cent_earned))
            else:
                newline.append(lastline[n])
        lastline = list(newline)  # save the line for use it in the next loop
        with open("tableau_prog_dynamique.csv", "a") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(newline)


def resolution(df, n, i, donnee, res):
    """
    resolve the table, determine the best solution
    :param df: data base pandas: the table of dynamic prog
    :param n: index of price
    :param i: index of action
    :param donnee: array of actions
    :param res: array of actions to purchase
    :return: res
    """
    if df.loc[df.index[i], n] == 0:
        return res
    elif i == 0:
        res.append(donnee[i])
        return res
    elif df.loc[df.index[i], n] == df.loc[df.index[i-1], n]:
        return resolution(df, n, i-1, donnee, res)
    else:
        res.append(donnee[i])
        return resolution(df, n-donnee[i].cent_price, i-1, donnee, res)

# dynamic program functions :


def glouton(donnee, money):
    """
    Sort actions with the best profit and in order buy them if there is enough money left
    :param donnee: array of actions
    :param money: money to use
    :return: Solution object
    """
    res = []
    donnee.sort(reverse=True)
    for action in donnee:
        if action.price <= money:
            money -= action.price
            res.append(action)
    return Solution(res)
