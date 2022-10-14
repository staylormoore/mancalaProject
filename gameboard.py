# Gameboard Class
class Gameboard:
    def __init__(self):
        # instance variables
        # initializes p1 and p2's side with 4 seeds in each pit
        # last element of p1 = their mancala, first element of p2 = their mancala
        self.p1pits = [4, 4, 4, 4, 4, 4, 0]
        self.p2pits = [0, 4, 4, 4, 4, 4, 4]
        self.board = [self.p1pits, self.p2pits]

    def __str__(self):
        return self.board

    def move_seeds(self, pit):

    def game_over(self):

        if self.p1pits