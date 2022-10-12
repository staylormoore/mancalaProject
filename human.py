from player import Player


class Human(Player):

    def __init__(self, n):
        self.name = n

    def move(self):
        self.pit = input("Select a pit (1-6):")
