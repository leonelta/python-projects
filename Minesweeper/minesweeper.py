import random
import re

#lets craeate a board object to represent the minesweeper game
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        #helper function
        self.board = self.make_new_board()
        self.assign_values_to_board()
        
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
            loc = random.randint(0, self.dim_size**2 - 1)#return a random integer N such that a<=N<= b
            row = loc // self.dim_size # the number of times dim_size into loc to tell us
            col = loc % self.dim_size # the remainder to tell us what index in that row to loc
            
            if board[row][col] == '*':
                continue
            
            board[row][col] = '*' #plant the bomb
            bombs_planted += 1
            
        return board
  
  
  
  
    def assign_values_to_board(self) :
        for r in range(self.dim_size) :
            for c in range(self.dim_size) :
                if self.board[r][c] == '*':
                    #if this is already a bomb , we don't want to calculate anything
                    continue
                self.board[r][c] = self.get_num_neighbouring_bombs(r, c)
                
    def get_num_neighbouring_bombs(self, row, col):
        num_neighbouring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row +1) + 1):
            for c in range(max(0, col-1), min(self.dim_size - 1, col+1)+ 1):
                if r == row and c == col:
                    continue
                if self.board[r][c]  == '*':
                    num_neighbouring_bombs += 1
                    
        return num_neighbouring_bombs
    
    def dig(self, row, col):
        #dig at that location
        #return True if successful dig , False if bomb dig
        
        #hit a bomb -> game over
        # dig at loctaion with neighbouring bombs -> finish dig
        # dig at loctaion with neighbouring bombs -> recursively dig neighbours!
        
        self.dug.add((row, col)) 
        
        if self.board[row][col] =='*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        #  self.board[row][col] == 0  
        for r in range(max(0, row-1), min(self.dim_size-1, row +1) + 1):
            for c in range(max(0, col-1), min(self.dim_size - 1, col+1)+ 1):
                if (r, c) in self.dug:
                    continue   # don't dig where you've already dug
                self.dig(r, c)  
        
        return True                                                               


    def __str__(self):
        # this is a function where if you call print on this object
        # it'll print out what this function returns!
        #return a string that shows the board to the player
        
        #create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if(row, col)in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
                    
        # put this together in a string
        
    #play the game
def play(dim_size = 10, num_bombs = 10):
    #step 1 : create the board and plant the bombs
    board = Board(dim_size, num_bombs)
    
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,c0l: "))
        row, col = int(user_input[0]), int(user_input[-1])
        