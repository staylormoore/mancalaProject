# Game Class
from human import Human
from gameboard import Gameboard


class Game:
    def __init__(self):
        self.gb = Gameboard()  # mancala board
        self.p1 = Human("Player1")  # player1
        self.p2 = Human("Player2")  # player2
        self.turn = True  # when turn = True, it is p1's turn, when turn = False, it is p2's turn

        print(self.g1.__str__())  # testing, can delete later
        print(self.p1.__str__())  # testing, can delete later

    def play(self):  # method that the client calls to play the game
        while not Gameboard.game_over():  # while the game is still going
            if self.turn:  # p1 move
                print("Player 1's turn")
                pit = self.p1.move()
                repeat = self.gb.move_seeds(pit, 1)
                if not repeat:
                    self.turn = False
            else:  # p2 move
                print("Player 2's turn")
                pit = self.p2.move()
                repeat = self.gb.move_seeds(pit, 2)
                if not repeat :
                    self.turn = True
    def determine_winner(self):  # determines which player wins by counting up the seeds in each pit once the
        # game is over
        p1seeds = self.gb.get_p1pits()
        p2seeds = self.gb.get_p2pits()
        if p1seeds[0] > p2seeds[6]:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
