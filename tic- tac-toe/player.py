import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    #we want all players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #get a random variable spot for the next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn, Input move (8-9):')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                    print('Invalid square. Try again.')
        
        return val

def GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) ==9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)
        return square

    def minimax(self, state, player):
        max_player = self.letter #yourself
        other_player = 'O' if player == 'X' else 'X'


        if state.current_winner  == other_player:
            return('poistion': None,
                   'score': 1*(state.num_empty_square() + 1) if other_player == max_player else -1 *(
                      state.num_empty_square() + 1 )
                   )

        elif not state.empty_squares():
            return('position': None, 'score': 0)

        if player == max_player:
            best = ('position': None, 'score': -math.inf)
        else:
            best = ('position': None, 'score': math.inf) #each score should minimize

        for possible_move in state.available_moves():
            #step 1: make a move, try that spot
            state.make_move(possible_move, player)
            #step 2: recurse using minimax to stimulate a game after making that move
            #step 3: undo the move

            #step 4: update the dictionaries if necessary
            


