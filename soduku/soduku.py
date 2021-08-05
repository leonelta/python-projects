def find_next_empty(puzzle):
    #finds the next row, col on the puzzle that's not filled yet --> rep with -1
    #return rowm col tuple (or(None, None) if there is none) 
    
    #keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
            
    return None, None # if no spaces in the puzzle are empty(-1)

def solve_sudoku(puzzle):
    #solve sudoku using backtracking!
    #our puzzle is a list of lists, where each inner list is a row inour sudoku puzzle
    #return whether solution exists
    #mutates puzzle to be the solution(if solution exists)
    
    #step 1: choose somewhere onthe puzzle to make a guess
    row, col = find_next_empty(puzzle)