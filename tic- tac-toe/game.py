class TicTacToe:
    def __init__(self):
        self.board = ['' for _ in range(9)] # we will use a single list to rep 3*3 board
        self.current_winner = None

    def print_board(self):
        #This is just getting the rows
        for row in [self.board[i*3:(i*1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + ' |')
            
    @staticmethod
    def print_board_nums():
        number_board = [[str(1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + '| '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == '']

    def empty_square(self):
        return '' in self.board

    def num_empty_square(self):
        return len(self.available_moves())
        
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
 