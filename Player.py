#
# ps10pr2.py  (Problem Set 10, Problem 2)
#
# A Connect-Four Player class 
#  

from ps10pr1 import Board

class Player():
    """ Connect Four Player Class
    """
    def __init__(self, checker):
        """ Player constructor with attributes checker and num_moves
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ Returns the identity of the specified Player object
        """
        return 'Player ' + self.checker

    def opponent_checker(self):
        """ returns the character representing the Player's opponent's checker
        """
        if self.checker == 'O':
            return 'X'
        else:
            return 'O'

    def next_move(self, board):
        """ Prompts the user to choose a column to drop a checker into.
            Will retry if the chosen input is invalid.
        """
        while True:
            c = int(input('Enter a column: '))
            if board.can_add_to(c):
                break
            else:
                print('Try Again!')
        self.num_moves += 1
        return c

def test():
    """ Test Cases """
    p = Player('X')
    b = Board(6, 7)    # valid column numbers are 0 - 6
    p.next_move(b)
    
            
        
        
