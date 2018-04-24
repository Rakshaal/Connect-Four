#
# ps10pr4.py  (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four   
#
import time
import random  
from ps10pr3 import *

class AIPlayer(Player):
    """ Implements an AIPlayer class with methods
        inherited from the Player class
    """

    def __init__(self, checker, tiebreak, lookahead):
        """ AIPlayer constructor with checker,
            tiebreaking strategy,and look-ahead value attributes
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ returns a string with the attributes of the AIPlayer
        """
        inh = super().__repr__()
        rep = inh + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return rep

    def max_score_column(self, scores):
        """ Determines the best column from a list of scores and breaks
            ties according to the called object's tiebreaking strategy
        """
        columns = []
        best = max(scores)
        for col in range(len(scores)):
            if scores[col] == best:
                columns += [col]
        if self.tiebreak == 'LEFT':
            return columns[0]
        elif self.tiebreak == 'RIGHT':
            return columns[-1]
        else:
            return random.choice(columns)

    def scores_for(self, board):
        """ returns the scores for each column for an AIPlayer
            with a given board state
        """
        if self.lookahead > 0:
            opp = AIPlayer(self.opponent_checker(), self.tiebreak, (self.lookahead-1))
        scores = [50]*board.width
        for col in range(board.width):

            if not(board.can_add_to(col)):
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50            
            else:
                board.add_checker(self.checker, col)
                oppscores = opp.scores_for(board)
                scores[col]= 100 - max(oppscores)
                board.remove_checker(col)
        return scores

    def next_move(self, board):
        """ returns the column of the best move for the called AIPlayer
            and increments the number of moves made
        """
        t = time.clock()
        col = self.max_score_column(self.scores_for(board))
        self.num_moves += 1
        t=time.clock()-t
        print(t)
        return col
                
                
def test():
    """ method testing
    """
    scores = [0, 0, 50, 0, 50, 50, 0]
    p1 = AIPlayer('X', 'LEFT', 1)
    p2 = AIPlayer('X', 'RIGHT', 1)
    p3 = AIPlayer('O', 'RANDOM', 2)
    print(p1.max_score_column(scores))
    print(p2.max_score_column(scores))
    print(p3.max_score_column(scores))
    print('-----------------------')
    b = Board(6,7)
    b.add_checkers('3042564121354')
    print(b)
    for i in range(7):
        p3.lookahead = i
        print(p3.scores_for(b))
        print('-------------------------------------------')
    
    
    
    

def testAI():
    """ Play Testing
    """
    p1 = AIPlayer('X', 'RANDOM', 6)
    p2 = AIPlayer('O', 'RANDOM', 6)
    p3 = Player('X')
    connect_four(p1, p2)
