from os import listdir
from os.path import isfile, join
from controller import *

def acceuil():
    fichiers = [f for f in listdir("donnees") if isfile(join("donnees", f))]
    print(fichiers)
    for i, file in enumerate(fichiers):
        print(i, " :", file)
    n=int(input("Veuiller selectioner le fichier de données d'action :"))
    programmes(getdonnee(fichiers[n]), input("combien d'argent voulez vous dépenser ? "))

def programmes(données, argent):
    print("Quel programme voulez vous utiliser ?\n Pour la méthode brutale tapez 1\n Pour la programation dynamique"
          " taper 2\n Pour l'algorithme glouton taper 3")
    n = input()
    print("début du calcul...")
    affichage(selectprog(n, données, argent))

def affichage(res):
    print(res[0])
    t = round(res[1], 2)
    print("le programme a mit ", str(t), "s à s'éxecuter.")

