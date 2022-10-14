# Gameboard Class
class Gameboard:
    def __init__(self):
        # instance variables
        # initializes p1 and p2's side with 4 seeds in each pit
        # last element of p1 = their mancala, first element of p2 = their mancala
        self.p1pits = [4, 4, 4, 4, 4, 4, 0]
        self.p2pits = [0, 4, 4, 4, 4, 4, 4]
        self.board = [self.p1pits, self.p2pits]




    def move_seeds(self, pit):
        pass

    def game_over(self):
        over = True
        for x in self.p1pits[0:6]:
            if self.p1pits[x] > 0:
                over = False
        for x in self.p2pits[-1:-7]:
            if self.p2pits[x] > 0:
                over = False
        return over
