# Human Subclass
from player import Player


class Human(Player):

    def __init__(self, n):
        self.name = n

    def __str__(self):  # to-string method for names
        return str(self.name)

    def move(self):  # returns the number that the user inputs as their seleted pit
        pit = int(input("Select a pit (1-6):"))
        return pit
