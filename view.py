from os import listdir
from os.path import isfile, join
from controller import *

def acceuil():
    print("Veuiller selectioner le fichier de données d'action :")
    fichiers = [f for f in listdir("donnees") if isfile(join("donnees", f))]
    print(fichiers)
    programmes(getdonnee(input("(Ecrire en toute lettre) ")), input("combien d'argent voulez vous dépenser ? "))

def programmes(données, argent):
    print("Quel programme voulez vous utiliser ?\n Pour la méthode brutale tapez 1\n Pour la programation dynamique"
          " taper 2\n Pour l'algorithme glouton taper 3")
    print("début du calcul...")
    affichage(selectprog(input(), données, argent))

def affichage(res):
    print(res[0])
    t = round(res[1], 2)
    print("le programme a mit ", str(t), "s à s'éxecuter.")

