# Gameboard Class
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

    def __str__(self):  # to-string for the board, prints p1pits and p2pits on separate lines
        print(self.p1pits)
        print(self.p2pits)
        return ""

    def move_seeds(self, pit, player_turn):  # method that determines how the seeds are sewn based on the player and
        # which pit they choose
        if player_turn == 1:  # if it is p1's turn
            seeds = self.p1pits[-pit]
            pit_num = -pit - 1
            self.p1pits[-pit] = 0  # sets # of seeds in pit that the user selected to zero
            p2pit_num = 0  # variable for when we have to place seeds in p2pits
            for x in range(seeds):  # number of times the loop runs = # of seeds in pit
                if pit_num < -7:  # if statement causes the seeds to loop around to p2pits if needed
                    self.p2pits[p2pit_num] += 1
                    p2pit_num += 1
                    if p2pit_num > 5:  # if it needs to loop again back to p1pits
                        pit_num = -1
                        p2pit_num = 0
                else:
                    self.p1pits[pit_num] += 1  # if it stays on p1pits' side, keep sewing the seeds on the correct side
                    pit_num -= 1
                if x == seeds - 1 and pit_num == -8 and p2pit_num == 0:  # if the last seed was placed in the mancala,
                    # repeat the player's turn
                    return True
            return False
        else:  # if it is p2's turn
            seeds = self.p2pits[pit-1]
            pit_num = pit
            self.p2pits[pit-1] = 0  # sets # of seeds in pit that the user selected to zero
            p1pit_num = -1  # variable for when we have to place seeds in p1pits
            for x in range(seeds):  # number of times the loop runs = # of seeds in pit
                if pit_num > 6:  # if statement causes the seeds to loop around to p1pits if needed
                    self.p1pits[p1pit_num] += 1
                    p1pit_num -= 1
                    if p1pit_num < -6:  # if it needs to loop again back to p2pits
                        pit_num = 0
                        p1pit_num = -1
                else:
                    self.p2pits[pit_num] += 1  # if it stays on p2pits' side, keep sewing the seeds on the correct side
                    pit_num += 1
                if x == seeds - 1 and pit_num == 7 and p1pit_num == -1:  # if the last seed was placed in the mancala,
                    # repeat the player's turn
                    return True
            return False

    def game_over(self):
        over = True
        # check to see if a board is full of zeros.
        # if either side is full of zeros return trure


        # in determine_winner():
        #traverse both, and add each sides pockets to the mancala
        # then compare mancalas
        for x in range(-1, -7, -1):  # this for loop checks each pit on player1's side for seeds
            if self.p1pits[x] > 0:  # if the pit has a seed in it, over is false which means the game is not finished
                over = False
            for y in range(7):  # this for loop checks each pit on player2's side for seeds
                if self.p2pits[y] > 0:  # if the pit has a seed in it, over is false which means the game is not finished
                    over = False
        return over
