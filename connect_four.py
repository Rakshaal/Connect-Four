#
# ps10pr3.py  (Problem Set 10, Problem 3)
#
# Playing the game 
#   

from ps10pr1 import Board
from ps10pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

def process_move(player, board):
    """ Processes the called player's next move
        and returns True if the game has ended
        and False if the game has not ended
    """
    print(player, '\'s turn')
    move = player.next_move(board)
    board.add_checker(player.checker, move)
    print()
    print(board)
    if board.is_win_for(player.checker):
        print(player, 'wins in', player.num_moves, 'moves.')
        return True
    elif board.is_full():
        print('It\'s a tie!')
        return True
    else:
        return False

class RandomPlayer(Player):
    """ Unintelligent AIPlayer Class with
        inherited methods from Player
    """

    def next_move(self, board):
        """ Randomly choosesa column from the non-full
            columns in the board an returns it's value
        """
        columns = []
        for col in range(board.width):
            if board.can_add_to(col):
                columns += [col]
        c = random.choice(columns)
        self.num_moves += 1
        return c
        
    
def test():
    """ test cases """
    b1 = Board(2, 4)
    p1 = Player('O')
    p2 = Player('X')
    b1.add_checkers('001122')
    process_move(p1, b1)
    process_move(p2, b1)
    p2 = Player('O')
    p1 = Player('X')
    connect_four(p1, p2)

def test_random():
    """ test cases """
    p1 = RandomPlayer('X')
    p2 = RandomPlayer('O')
    connect_four(p1,p2)


    
    
    
