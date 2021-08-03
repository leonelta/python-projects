#lets craeate a board object to represent the minesweeper game
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        #we'll save (row,col) tuples into this set
        self.dug = set()
      
#play the game
def play(dim_size = 10, num_bombs = 10):
    pass