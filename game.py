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
        while not self.gb.game_over():  # while the game is being played
            if self.turn:  # p1's turn
                print("Player 1's turn")
                pit = self.p1.move()
                repeat = self.gb.move_seeds(pit, 1)
                print(self.gb.__str__())
                if not repeat:  # if p1's last seed doesn't go into their mancala, it is p2's turn
                    self.turn = False
            else:  # p2's turn
                print("Player 2's turn")
                pit = self.p2.move()
                repeat = self.gb.move_seeds(pit, 2)
                print(self.gb.__str__())
                if not repeat:  # if p2's last seed doesn't go into their mancala, it is p1's turn
                    self.turn = True
        self.determine_winner()

    def determine_winner(self):  # determines which player wins by counting up the seeds in each pit once the
        # game is over
        p1pits_dup = self.gb.get_p1pits()  # duplicate lists for p1pits and p2pits by using the accessor method
        p2pits_dup = self.gb.get_p2pits()
        p1seeds = 0
        p2seeds = 0
        for x in range(-1, -8, -1):  # iterates through p1pits, getting the # of seeds that may be leftover
            p1seeds += p1pits_dup[x]
        for x in range(7):  # iterates through p2pits, getting the # of seeds that may be leftover
            p2seeds += p2pits_dup[x]
        print("Player 1 gets ", p1seeds, "seeds and Player 2 gets ", p2seeds, "seeds")
        if p1seeds > p2seeds:
            print("Player 1 wins!")  # if p1 has more seeds, p1 wins
        elif p2seeds > p1seeds:  # if p2 has more seeds, p2 wins
            print("Player 2 wins!")
        else:
            print("Draw!")  # if p1's seeds equals p2's seeds, it is a draw
