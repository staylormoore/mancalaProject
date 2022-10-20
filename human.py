# Human Subclass
from player import Player
from gameboard import Gameboard
from game import Game


class Human(Player):

    def __init__(self, n):
        self.name = n

    def __str__(self):  # to-string method for names
        return str(self.name)

    def move(self):
        pit = input("Select a pit (1-6):")
        return pit-1  # minus one so that the user doesn't have to enter "pit zero"

