# AI Player for use in Connect Four  

import random  
from player_random import *

class AIPlayer(Player):
    """ an AI player who chooses moves based on how far it can lookahead and /
        and the way it deals with tiebreaks
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ constructor function which initializes checker, tiebreak and lookahead
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ returns a string to represent that represents the AI player
        """
        return 'Player ' + str(self.checker) + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'

    def max_score_column(self, scores):
        """ parameter: a list scores containing a score for each column
            returns the score of the maximum colnum and returns specific colnum /
            based on tiebreak method
        """
        max_num = max(scores)
        max_list = []
        for x in range(len(scores)):
            if scores[x] == max_num:
                max_list += [x]
        if self.tiebreak == 'LEFT':
            return max_list[0]
        if self.tiebreak == 'RIGHT':
            return max_list[-1]
        else:
            return random.choice(max_list)
        
    def scores_for(self, b):
        """ returns a list of scores - one for each col in board b
        """
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, (self.lookahead - 1))
                opp_scores = opponent.scores_for(b)
                if max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 50:
                    scores[col] = 50
                elif max(opp_scores) == 0:
                    scores[col] = 100
                b.remove_checker(col)
                
        return scores
        
    def next_move(self, b):
        """ returns the best move according to AIPlayer's judgement methods
        """
        scores = self.scores_for(b)
        return self.max_score_column(scores)
        
        
        
        
        