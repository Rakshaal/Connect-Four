class Board():
    """ Connect Four Board Class which can initialize Board objects of arbitrary widths and heights
    """

    def __init__(self, height, width):
        """ Board constuctor with attributes height, width, and slots
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a text representation of the board
        """
        board = ''
        for row in range(self.height):
            board += '|'
            for col in range(self.width):
                board += self.slots[row][col] + '|'
            board += '\n'
        bot = (2*self.width + 1) * '-' 
        board += bot + '\n'
        board += ' '
        for col in range(self.width):
            board += str(col%10) + ' '
        return board

    def add_checker(self, checker, col):
        """ Adds a checker to the specified column
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        for row in range(1, self.height + 1):
            p = abs(row - self.height)
            if self.slots[p][col] == ' ':
                self.slots[p][col] = checker
                break

    def reset(self):
        """ Clears the board of all checkers
        """
        self.slots = [[' '] * self.width for row in range(self.height)]

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ Returns True if the column is not full, False otherwise
        """
        if (col < 0) or (col >= self.width):
            return False
        elif self.slots[0][col] != ' ':
            return False
        else:
            return True

    def is_full(self):
        """ Returns True if the Board is entirely full, False otherwise
        """
        for col in range(self.width):
            if self.can_add_to(col):
                return False
        return True

    def remove_checker(self, col):
        """ Removes the topmost checker from the specified column
        """
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False
    def is_down_diagonal_win(self, checker):
        """ Checks for a diagonal down from left to right win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False
            
    def is_up_diagonal_win(self, checker):
        """ Checks for a diagonal up from left to right win for the specified checker.
        """
        for row in range(self.height-3):
            for col in range(3, self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col - 1] == checker and \
                   self.slots[row + 2][col - 2] == checker and \
                   self.slots[row + 3][col - 3] == checker:
                    return True
        return False

    def is_win_for(self, checker):
        """ put your docstring here
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) or \
           self.is_vertical_win(checker) or \
           self.is_down_diagonal_win(checker) or \
           self.is_up_diagonal_win(checker):
            return True
        else:
            return False
            


def test():
    b = Board(6, 7)
    print(b)
    b.add_checker('X', 0)
    print(b)
    b.add_checker('X', 0)
    b.add_checker('O', 0)
    b.add_checker('X', 0)
    b.add_checker('O', 3)
    b.add_checker('O', 4)    # cheat and let O go again!
    b.add_checker('O', 5)
    b.add_checker('O', 6)
    print(b)
    b.reset()
    print(b)
    b = Board(1,1)
    print(b)
    print(b.can_add_to(0))
    print(b.can_add_to(1))
    print(b.can_add_to(-1))
    print('It is ' + str(b.is_full()) + ' that the board is full')
    b.add_checker('X', 0)
    print(b)
    print(b.can_add_to(0))
    print('It is ' + str(b.is_full()) + ' that the board is full')
    b = Board(2, 2)
    b.add_checkers('0011')
    print(b)
    b.remove_checker(1)
    b.remove_checker(1)
    b.remove_checker(1)     # column empty; should have no effect
    b.remove_checker(0)
    print(b)
    b = Board(6, 7)
    b.add_checkers('00102030')
    print(b)
    print(b.is_win_for('X'))
    print(b.is_win_for('O'))
    b.reset()
    b.add_checkers('23344545515')
    print(b)
    print(b.is_win_for('X'))
    print(b.is_win_for('O'))
    b.reset()
    b.add_checkers('2222334364051')
    print(b)
    print(b.is_win_for('X'))
    print(b.is_win_for('O'))
