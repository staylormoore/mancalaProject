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
                if x == seeds - 1 and pit_num > -8 and self.p1pits[pit_num + 1] == 1:  # if the last seed was placed in
                    # an empty pit on your own side, do the capture series
                    self.capture_series(1, pit_num + 1)
                if x == seeds - 1 and pit_num == -8 and p2pit_num == 0:  # if the last seed was placed in the mancala,
                    # repeat the player's turn
                    return True
            return False
        else:  # if it is p2's turn
            seeds = self.p2pits[pit - 1]
            pit_num = pit
            self.p2pits[pit - 1] = 0  # sets # of seeds in pit that the user selected to zero
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
                if x == seeds - 1 and pit_num < 7 and self.p2pits[pit_num - 1] == 1:
                    self.capture_series(2, pit_num - 1)
                if x == seeds - 1 and pit_num == 7 and p1pit_num == -1:  # if the last seed was placed in the mancala,
                    # repeat the player's turn
                    return True
            return False

    def capture_series(self, player_turn, pit):  # method runs if the player's last seed is placed in an empty pit on their side and
        # loops through to the opponent's side and captures the seed across, leaving the capturing seed that was
        # placed on their side
        # modification: any pits with two seeds on the opponent's side are also captured
        if player_turn == 1:
            pass
        else:
            captured_pit = (pit + 1) - 7
            captured_seeds = self.p1pits[captured_pit]
            self.p1pits[captured_pit] = 0
            self.p2pits[6] += captured_seeds

    def game_over(self):  # method checks to see if one of the rows of pits is all zeros, ending the game if it is
        p1_sum = 0
        p2_sum = 0
        for x in range(-1, -7, -1):  # this for loop checks each pit on player1's side for seeds
            p1_sum += self.p1pits[x]
        for y in range(6):  # this for loop checks each pit on player2's side for seeds
            p2_sum += self.p2pits[y]
        if p1_sum > 0 and p2_sum > 0:  # if there are seeds left in both rows of pits, return False
            return False
        return True
