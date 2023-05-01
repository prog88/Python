# Class Terminal View
class Terminal:
    def __init__(self):
        pass

    def display(self, board_str):
        print(board_str)
   
    def display_tie(self):
        print("It's a Tie!")
    
    def display_scores(self, symbol_str, wins_str):
            print(f"{symbol_str} : {wins_str}")

    def display_winner(self, symbol):
        print(f"Congratulations, player {symbol} has won!")