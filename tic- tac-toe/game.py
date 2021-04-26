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
        return self.board.count('')

    def make_move(self, square, letter):
        #if valid move, then save the move (assign square to letter)
        #then return True. if invalid, return False

        if self.board[square] == '':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #winner if 3 in arow anywhere.. we have to check all of these!
        # first let's check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all ([spot == letter for spot in row]):
            return True

        #check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + 'makes a move to square {square}')
                game.print_board()
                print('') #just empty line

            if game.current_winner:
                if print_game:
                    print(letter + 'wins!')
                return letter

            #after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'
           # if letter == 'X':
           #     letter = 'O'
           # else:
           #     letter = 'X'

             #BUT WAIT WHAT IF WE WON??

        if print_game:
            print('It\'s a tie!')
