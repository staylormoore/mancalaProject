# Game Class
from human import Human
from gameboard import Gameboard


class Game:
    g1 = Gameboard()  # mancala gameboard
    p1 = Human()  # player1
    p2 = Human()  # player2

    print(g1)
