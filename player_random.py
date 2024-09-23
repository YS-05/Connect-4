# Playing the game  

from board_setup import Board
from player_setup import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

def process_move(p, b):
    """ parameter: a Player object p and a Board object b /
        prints who's turn it is, processes it and informs the result
    """
    print(str(p.__repr__()) + "'s turn")
    move_col = p.next_move(b)
    b.add_checker(p.checker, move_col)
    p.num_moves += 1
    print()
    print(b)
    if b.is_win_for(p.checker) == True:
        print(str(p.__repr__()) + ' wins in ' + str(p.num_moves) + ' moves.')
        print('Congratulations!')
        return True
    elif b.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False
        
class RandomPlayer(Player):
    """ an AI player who chooses random legal columns
    """

    def next_move(self, b):
        """ parameter: a Board object
            returns the column where the user wants to place the checker
        """
        free_col = []
        for c in range(b.width):
            if b.can_add_to(c) == True:
                free_col += [c]
        random_col = random.choice(free_col)
        return random_col