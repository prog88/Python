from Models.player import Player
from Models.board import Board
from Views.terminal import Terminal

# Class TicTacToeTerm
class TicTacToeTerm:
    def __init__(self, board, players, terminal_view):
        self.board = board
        self.players = players
        self.current_player = self.players[0]
        self.terminal_view = terminal_view

    def get_move(self, player):
        move_str = input(f"Player {player}, enter row and column (e.g. 1 2): ")
        try:
            row, col = map(int, move_str.split())
            return 3*(row-1) + (col-1)
        except ValueError:
            print("Invalid input. Try again.")
            return self.get_move(player)

    def get_state(self, board):
        board_str = "  1 2 3\n"
        for row in range(3):
            board_str += str(row + 1) + " "
            for col in range(3):
                index = row * 3 + col
                board_str += board.grid[index] + " "
            board_str += "\n"
        return board_str

    def display_scores(self, players):
        for player in players: 
            terminal_view.display_scores(player.symbol, player.wins)

    def play(self):
        while True:
            terminal_view.display(self.get_state(self.board))
            index_position = self.get_move(self.current_player.symbol)
            self.board.make_move(index_position, self.current_player.symbol)

            if self.board.check_win():
                terminal_view.display(self.get_state(self.board))
                terminal_view.display_winner(self.current_player.symbol)
                self.current_player.add_win()
                break

            if self.board.is_full():
                terminal_view.display(self.get_state(self.board))
                terminal_view.display_tie()
                break

            self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
        self.display_scores(self.players)

# Exec
if __name__ == "__main__":
    board = Board()
    players = [Player("X"), Player("O")]
    terminal_view = Terminal()
    game = TicTacToeTerm(board, players, terminal_view)
    game.play()

