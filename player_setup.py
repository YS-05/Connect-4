# A Connect-Four Player class 

from board_setup import Board

class Player:
    def __init__(self, checker):
        """parameter: checker
           constructs a new player object initializing checker and num_moves
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """returns a string representing a player object, shows which checker player using
        """
        return 'Player ' + str(self.checker)
    
    def opponent_checker(self):
        """returns the checker of opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """ parameter: Board object b
            returns the column where the players wants to make the next legal move/
            keeps asking for column until legal column to place found
        """
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                self.num_moves += 1
                return col
            else:
                print('Try again!')
                print()