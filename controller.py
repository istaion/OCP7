from view import *
from model import *
from time import time
import csv
import pandas as pd

def getdonnee(file) :
    data = pd.read_csv("donnees/" + file)
    liste_actions = []
    for item in data.values:
        liste_actions.append(Action(item))
    return liste_actions

def selectprog(number, donnees, argent):
    t1 = time()
    if number == '1':
        res = brutalforce(donnees, argent)
        return (res, time()-t1)
    elif number == '2':
        res = dynamicprog(donnees, argent)
        return (res, time() - t1)
    else:
        print('prout')

def brutalforce(donnees, argent):
    with open('brutalsolutions.csv', 'w'):
        pass
    keys = ['benefice']
    for action in donnees:
        keys.append(action.name)
    with open('brutalsolutions.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(keys)
    denombrement(donnees, argent, [])
    df = pd.read_csv('brutalsolutions.csv')
    df = df.sort_values(by = 'benefice', ascending=False)
    soluc = []
    for action in donnees:
        if action.is_in_solution(df.iloc[0]):
            soluc.append(action)
    soluc = Solution(soluc)
    return soluc



def denombrement(list_actions, money, res):
    money = int(money)
    if len(list_actions) == 0:  # S'il n'y a plus d'actions à envisager on calcul le bénéfice et on ajoute la solution au csv
        benefice = 0
        for action in res:
            benefice += action[0].earned * action[1]
        value = [benefice]
        for action in res:
            value.append(action[1])
        with open('brutalsolutions.csv', 'a') as csv_file:
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
