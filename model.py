class Action:
    """
    Object action with price in euros or cent, profit in percentage, money earned in euros or cent
    """
    def __init__(self, action):
        self.name = action[0]
        self.price = round(action[1], 2)
        self.profit = round(action[2], 2)
        self.earned = round(action[1] * action[2]/100, 2)
        self.cent_price = int(round(action[1] * 100))
        self.cent_earned = int(round(action[1] * action[2]))

    def __repr__(self):
        return self.name

    def is_in_solution(self, solution):
        """
        check if the action is purchased in the solution
        :param solution: pandas data with the best possibility
        :return: boolean : true for purchase
        """
        if solution[self.name] == 1:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.profit < other.profit:
            return True
        else:
            return False

    def __le__(self, other):
        if self.profit <= other.profit:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.profit == other.profit:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.profit != other.profit:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.profit > other.profit:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.profit >= other.profit:
            return True
        else:
            return False


class Solution:
    """
    list of actions to buy. Calcul the benefice and the price.
    """
    def __init__(self, actions):
        self.actions = actions
        benefice = 0
        prix = 0
        for item in self.actions:
            benefice += item.earned
            prix += item.price
        self.benefice = benefice
        self.prix = prix

    def __repr__(self):
        res = "La meilleure solution est d'acheter les actions : "
        for item in self.actions:
            res += item.name + ", "
        res += "pour un b??nefice de : " + str(round(self.benefice, 2)) + "euros et un prix de :" \
               + str(round(self.prix, 2)) + "euros."
        return res
