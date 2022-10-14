# Human Subclass
from player import Player
from gameboard import Gameboard


class Human(Player):

    def __init__(self, n):
        self.name = n

    def move(self):
        pit = input("Select a pit (1-6):")
        Gameboard.move_seeds(pit)
