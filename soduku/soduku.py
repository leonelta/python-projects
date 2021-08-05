def find_next_empty(puzzle):
    #finds the next row, col on the puzzle that's not filled yet --> rep with -1
    #return rowm col tuple (or(None, None) if there is none) 
    
    #keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
            
    return None, None # if no spaces in the puzzle are empty(-1)

def is_valid(puzzle, guess, row, col):
    #figures whether guess at the row/col of the puzzle is a valid guess
    #return true if valid but false otherwise
    
    #let's begin with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # continue with column
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
        col_vals = [puzzle[i][col] for i in range(9)]
        if guess in col_vals:
            return False
        
    #aand then the square
    #we want to get where the x3 square starts
    #and iterate over the  values in the row/column
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

def solve_sudoku(puzzle):
    #solve sudoku using backtracking!
    #our puzzle is a list of lists, where each inner list is a row inour sudoku puzzle
    #return whether solution exists
    #mutates puzzle to be the solution(if solution exists)
    
    #step 1: choose somewhere onthe puzzle to make a guess
    row, col = find_next_empty(puzzle)
    
    #step 1.1: if there's no space left, then we're done because we only allowed valid inputs
    if row is None:
        return True
    
    #step 2: if there is a place to put a number, then make a guess btw 1 and 9
    for guess in range(1, 10): #range(1,10) is 1,2 ...9
        #step 3: check if this a valid guess
        if is_valid(puzzle, guess, row, col):