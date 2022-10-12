class Gameboard:
    def __init__(self, g):
        self.gameboard = g

    p1pits = [4, 4, 4, 4, 4, 4, 0]  # initializes p1's side with 4 seeds in each pit, last element = their mancala
    p2pits = [0, 4, 4, 4, 4, 4, 4]  # initializes p2's side with 4 seeds in each pit, first element = their mancala

