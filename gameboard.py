# Gameboard Class
from game import Game
class Gameboard:
    def __init__(self):
        # instance variables
        # initializes p1 and p2's side with 4 seeds in each pit
        # last element of p1 = their mancala, first element of p2 = their mancala
        self.p1pits = [0, 4, 4, 4, 4, 4, 4]
        self.p2pits = [4, 4, 4, 4, 4, 4, 0]
        self.board = [self.p1pits, self.p2pits]

    def get_p1pits(self):  # accessor method for p1pits --> enables to be used in other classes
        return self.p1pits

    def get_p2pits(self):  # accessor method for p2pits --> enables to be used in other classes
        return self.p2pits

    def __str__(self):  # to-string for the board
        return str(self.board)

    def move_seeds(self, pit, turn):  # method that determines how the seeds are sewn based on the player and
        # which pit they choose
        if turn == 1:



    def game_over(self):
        over = True
        for x in self.p1pits[0:6]:  # this for loop checks each pit on player1's side for seeds
            if self.p1pits[x] > 0:  # if the pit has a seed in it, over is false which means the game is not finished
                over = False
        for x in self.p2pits[-1:-7]:  # this for loop checks each pit on player2's side for seeds
            if self.p2pits[x] > 0:  # if the pit has a seed in it, over is false which means the game is not finished
                over = False
        return over
