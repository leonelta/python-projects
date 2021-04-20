class TicTacToe:
    def __init__(self):
        self.board = ['' for _ in range(9)] # we will use a single list to rep 3*3 board
        self.current_winner = None