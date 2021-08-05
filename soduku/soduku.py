def find_next_empty(puzzle):

def solve_sudoku(puzzle):
    #solve sudoku using backtracking!
    #our puzzle is a list of lists, where each inner list is a row inour sudoku puzzle
    #return whether solution exists
    #mutates puzzle to be the solution(if solution exists)
    
    #step 1: choose somewhere onthe puzzle to make a guess
    row, col = find_next_empty(puzzle)