from view import *
from model import *
from time import time
import csv
import pandas as pd

def getdonnee(file) :
    data = pd.read_csv("donnees/" + file)
    liste_actions = []
    for item in data.values:
        if item[1]<=0:
            pass
        else:
            liste_actions.append(Action(item))
    return liste_actions

def selectprog(number, donnees, money):
    money = float(money)
    t1 = time()
    if number == 1:
        res = brutalforce(donnees, money)
        return (res, time()-t1)
    elif number == 2:
        res = dynamicprog(donnees, money)
        return (res, time() - t1)
    else :
        res = glouton(donnees, money)
        return (res, time() - t1)

def brutalforce(donnees, argent):
    keys = ["benefice"]
    for action in donnees:
        keys.append(action.name)
    with open("brutalsolutions.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(keys)
    denombrement(donnees, argent, [])
    df = pd.read_csv("brutalsolutions.csv")
    df = df.sort_values(by = "benefice", ascending=False)
    soluc = []
    for action in donnees:
        if action.is_in_solution(df.iloc[0]):
            soluc.append(action)
    soluc = Solution(soluc)
    return soluc



def denombrement(list_actions, money, res):
    if len(list_actions) == 0:  # S'il n'y a plus d'actions à envisager on calcul le bénéfice et on ajoute la solution au csv
        benefice = 0
        for action in res:
            benefice += action[0].earned * action[1]
        value = [benefice]
        for action in res:
            value.append(action[1])
        with open("brutalsolutions.csv", "a") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(value)
    else:  # On selection la première action et on réapelle la fonction sans l'acheter et en l'achetant s'il reste
        # assez d'argent
        action_selected = list_actions[0]
        newlist = list(list_actions)
        newlist.pop(0)
        res0 = list(res)
        res0.append((action_selected, 0))
        denombrement(newlist, money, res0)
        if money >= action_selected.price:
            res1 = list(res)
            res1.append((action_selected, 1))
            denombrement(newlist, money - action_selected.price, res1)

def dynamicprog(donnee, argent):
    money = round(float(argent) * 100)
    creationtab(donnee, money)
    tab = pd.read_csv("tableau_prog_dynamique.csv", header = None)
    soluc = resolution(tab, money, len(donnee)-1, donnee, [])
    return Solution(soluc)

def creationtab(donnee, money):
    with open("tableau_prog_dynamique.csv", "w"):
        pass
    for i, action in enumerate(donnee):
        newline = []
        for n in range(money+1):
            if i==0:
                if n >= action.cent_price:
                    newline.append(action.cent_earned)
                else:
                    newline.append(0)
            elif n >= action.cent_price:
                newline.append(max(lastline[n], lastline[n-action.cent_price]+action.cent_earned))
            else:
                newline.append(lastline[n])
        lastline = list(newline)
        with open("tableau_prog_dynamique.csv", "a") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(newline)

def resolution(df, n, i, donnee, res):
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

def glouton(donnee, money):
    res = []
    donnee.sort(reverse = True)
    for action in donnee:
        if action.price <= money:
            money -= action.price
            res.append(action)
    return Solution(res)

def error_input(res, n, m):
    res = int(res)
    while res < n or res > m:
        print("veuillez entrer un nombre entre ", n, " et ", m,":")
        res = int(input())
    return res
