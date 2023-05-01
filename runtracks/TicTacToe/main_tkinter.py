import tkinter as tk
from Models.player import Player
from Models.board import Board

# Class TicTacToeUI 
class TicTacToeUI:
    def __init__(self, board, players):
        self.players = players
        self.current_player = players[0]
        self.board = board

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        # Create the label to display the game information
        self.info_label = tk.Label(self.root, text=f"Player {self.current_player.symbol}'s turn", font=("Arial", 16), pady=10)
        self.info_label.grid(row=0, column=0, columnspan=3)

        # Create the labels to display the board
        self.labels = []
        for i in range(3):
            row = []
            for j in range(3):
                label = tk.Label(self.root, text=" ", font=("Arial", 32), width=4, height=2, relief="ridge")
                label.grid(row=i+1, column=j, padx=5, pady=5)
                label.bind("<Button-1>", self.clicked_label)
                row.append(label)
            self.labels.append(row)

    # Actions
    def clicked_label(self, event):
        label = event.widget
        row, col = label.grid_info()["row"]-1, label.grid_info()["column"]
        position = 3*row + col

        if self.board.make_move(position, self.current_player.symbol):
            label.config(text=self.current_player.symbol)

            if self.board.check_win():
                self.show_winner()
            elif self.board.is_full():
                self.show_tie()
            else:
                self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
                self.info_label.config(text=f"Player {self.current_player.symbol}'s turn")

    # Display
    def show_winner(self):
        winner = self.current_player
        winner.add_win()
        self.current_player = None
        self.info_label.config(text=f"Player {winner.symbol} wins! ({winner.wins})")
        self.reset_board()

    def show_tie(self):
        self.current_player = None
        self.info_label.config(text="It's a tie!")
        self.reset_board()

    def reset_board(self):
        self.board = Board()
        self.current_player = self.players[0]
        for row in self.labels:
            for label in row:
                label.config(text=" ")

    # Life Cycle
    def run(self):
        self.root.mainloop()

# Exec
if __name__ == "__main__":
    board = Board()
    players = [Player("X"), Player("O")]
    game = TicTacToeUI(board, players)
    game.run()