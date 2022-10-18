# Game Class
from human import Human
from gameboard import Gameboard


class Game:
    g1 = Gameboard()  # mancala board
    p1 = Human("Player1")  # player1
    p2 = Human("Player2")  # player2

    print(g1.__str__())
    print(p1.__str__())


def determine_winner():
    p1seeds = g1.p1pits[0]
    p2seeds = g1.p2pits[7]
    if p1seeds > p2seeds:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")