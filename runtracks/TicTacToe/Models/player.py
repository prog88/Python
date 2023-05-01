# Class Player Model
class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.wins = 0

    def add_win(self):
        self.wins += 1