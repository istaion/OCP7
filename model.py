class Action:
    def __init__(self, action):
        self.name = action[0]
        self.price = round(action[1], 2)
        self.profit = round(action[2], 2)
        self.earned = round(action[1] * action[2], 2)
        self.cent_price = round(action[1] * 100)
        self.cent_earned = round(action[1] * action[2] * 100)

    def __repr__(self):
        return self.name

    def is_in_solution(self, solution):
        if solution[self.name] == 1:
            return True
        else:
            return False

class Solution:
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
        res += "pour un bénefice de : " + str(round(self.benefice, 2)) + "euros et un prix de :" \
               + str(round(self.prix, 2)) + "euros."
        return res
