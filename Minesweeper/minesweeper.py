import random

#lets craeate a board object to represent the minesweeper game
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        #helper function
        self.board = self.make_new_board()
        
        #we'll save (row,col) tuples into this set
        self.dug = set()
    
        # construct a new board based on the dim size amd num bombs
    def make_new_board(self):
        
        #generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        #this creates an array like this:
        #[[None, None,..., None],
        # [None, None,..., None],
        # [...]
        # [None, None,..., None]]
        
        #plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
        
      
#play the game
def play(dim_size = 10, num_bombs = 10):
    pass