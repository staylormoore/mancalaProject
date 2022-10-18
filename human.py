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
        turn = Game.whose_turn(self)
        if turn == True:
            print("Player 1's turn")
        else:
            print("Player 2's turn")
        pit = input("Select a pit (1-6):")
        Gameboard.move_seeds(pit)
