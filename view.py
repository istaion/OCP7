from os import listdir
from os.path import isfile, join
import controller as co


def acceuil():
    """
    request the choice of a file and the amount of money to spend
    :return:
    """
    files = [f for f in listdir("donnees") if isfile(join("donnees", f))]
    if len(files) == 0:
        print("Veuiller ajouter un ficher csv avec les actions disponible dans le dossier donnees.")
        exit()
    print(files)
    for i, file in enumerate(files):
        print(i, " :", file)
    n = int(co.error_input(input("Veuiller selectioner le fichier de données d'action :"), 0, len(files)-1))
    programmes(co.getdonnee(files[n]), input("combien d'argent voulez vous dépenser ? "))


def programmes(data, money):
    """
    ask which program to use
    :param data: array of actions
    :param money: money to spend
    :return:
    """
    print("Quel programme voulez vous utiliser ?\n Pour la méthode brutale tapez 1\n Pour la programation dynamique"
          " taper 2\n Pour l'algorithme glouton taper 3")
    n = co.error_input(input(), 1, 3)
    print("début du calcul...")
    print_solution(co.select_program(n, data, money))


def print_solution(res):
    """
    print the solution
    :param res: a tuple with solution objet and time spend
    :return:
    """
    print(res[0])
    t = round(res[1], 2)
    print("le programme a mit ", str(t), "s à s'éxecuter.")
