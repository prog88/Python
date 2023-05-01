# Class Board Model
class Board:
    def __init__(self):
        self.grid = [" " for _ in range(9)]

    def place_piece(self, index, player):
        if self.grid[index] != " ":
            raise ValueError("Cell already occupied.")
        self.grid[index] = player

    def make_move(self, index, symbol):
        try:
            self.place_piece(index, symbol)
        except ValueError as e:
            print(str(e))
            return False
        return True

    def check_win(self):
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
            (0, 4, 8), (2, 4, 6)              # diagonal
        ]
        for comb in win_combinations:
            if self.grid[comb[0]] == self.grid[comb[1]] == self.grid[comb[2]] != " ":
                return True
        return False

    def is_full(self):
        return " " not in self.grid