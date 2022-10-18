# Game Class
from human import Human
from gameboard import Gameboard


class Game:
    def __init__(self):
        self.g1 = Gameboard()  # mancala board
        self.p1 = Human("Player1")  # player1
        self.p2 = Human("Player2")  # player2
        self.turn = True  # when turn = True, it is p1's turn, when turn = False, it is p2's turn

        print(self.g1.__str__())
        print(self.p1.__str__())

    def determine_winner(self):
        p1seeds = self.g1.get_p1pits()  # FIX THIS - use accessor methods?
        p2seeds = self.g1.get_p2pits()
        if p1seeds[0] > p2seeds[6]:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
