# Game Class
from human import Human
from gameboard import Gameboard


class Game:
    self.g1 = Gameboard()  # mancala board
    p1 = Human("Player1")  # player1
    p2 = Human("Player2")  # player2
    turn = True  # when turn = True, it is p1's turn, when turn = False, it is p2's turn

    print(g1.__str__())
    print(p1.__str__())


def determine_winner():
    p1seeds = self.g1.p1pits[0]  # FIX THIS - use accessor methods?
    p2seeds = g1.p2pits[7]
    if p1seeds > p2seeds:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

