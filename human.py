# Human Subclass
from player import Player


class Human(Player):

    def __init__(self, n):
        self.name = n

    def __str__(self):  # to-string method for names
        return str(self.name)

    def move(self):  # returns the number that the user inputs as their selected pit
        pit = int(input("Select a pit (1-6):"))
        if pit > 6:  # prevents user from inputting an invalid pit index
            print("Please enter a valid pit number")
            return self.move()
        return pit
