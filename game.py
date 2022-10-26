# Game Class
from human import Human
from gameboard import Gameboard


class Game:
    def __init__(self):
        self.gb = Gameboard()  # mancala board
        self.p1 = Human("Player1")  # player1
        self.p2 = Human("Player2")  # player2
        self.turn = True  # when turn = True, it is p1's turn, when turn = False, it is p2's turn

    def play(self):  # method that the client calls to play the game
        print(self.gb.__str__())
        while not self.gb.game_over():  # while the game is still going
            if self.turn:  # p1 move
                print("Player 1's turn")
                pit = self.p1.move()
                repeat = self.gb.move_seeds(pit, 1)
                print(self.gb.__str__())
                if not repeat:
                    self.turn = False
            else:  # p2 move
                print("Player 2's turn")
                pit = self.p2.move()
                repeat = self.gb.move_seeds(pit, 2)
                print(self.gb.__str__())
                if not repeat:
                    self.turn = True

    def determine_winner(self):  # determines which player wins by counting up the seeds in each pit once the
        # game is over
        p1pits_dup = self.gb.get_p1pits()  # duplicate lists for p1pits and p2pits by using the accessor method
        p2pits_dup = self.gb.get_p2pits()
        p1seeds = 0
        p2seeds = 0
        for x in p1pits_dup:  # iterates through p1pits, getting the # of seeds that may be leftover
            p1seeds += p1pits_dup[x]
        for x in p2pits_dup:  # iterates through p2pits, getting the # of seeds that may be leftover
            p2seeds += p2pits_dup[x]
        if p1seeds > p2seeds:  # if p1 has more seeds, they win, else, p2 wins
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
