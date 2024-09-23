# Setting up the board and methods for the game

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.slots = [[' '] * width for row in range(height)]

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''       

        for row in range(self.height):
            s += '|' 

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  

        s += '-' * (self.width * 2 + 1) + '\n'
        
        for col in range(self.width):
            s += ' '
            num = col % 10
            s += str(num)
        
        s += '\n'
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
                
        for r in range(self.height - 1):
            if self.slots[r + 1][col] == 'X' or self.slots[r + 1][col] == 'O':
                self.slots[r][col] = checker
                break
            elif r + 1 == (self.height - 1):
                self.slots[r + 1][col] = checker

                    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X' 

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
                
    def reset(self):
        """resets board setting all slots to contain a space character
        """
        for r in range(self.height):
            for c in range(self.width):
                self.slots[r][c] = ' '
                    
    def can_add_to(self, col):
        """returns True if valid place for a checker, False if not
        """
        if 0 <= col <= self.width - 1:
            if self.slots[0][col] == ' ':
                return True
        return False
    
    def is_full(self):
        """returns True if board filled with checkers, False otherwise
        """
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        return True
                
    def remove_checker(self, col):
        """removes top checker from given column, stays same if empty column
        """
        for r in range(self.height):
            if self.slots[r][col] == 'X' or self.slots[r][col] == 'O':
                self.slots[r][col] = ' '
                break        
        
    def is_win_for(self, checker):
        """returns True if player has won game, False if not
        """
        if self.is_horizontal_win(checker) == True or self.is_vertical_win(checker) == True or self.is_diagonal_win(checker) == True:
            return True
        else:
            return False
    
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
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
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                    self.slots[row + 2][col] == checker and \
                    self.slots[row + 3][col] == checker:
                     return True

        return False
    
    def is_diagonal_win(self, checker):
        """ Checks for a diagonal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                    self.slots[row + 2][col + 2] == checker and \
                    self.slots[row + 3][col + 3] == checker:
                        return True
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row - 1][col + 1] == checker and \
                    self.slots[row - 2][col + 2] == checker and \
                    self.slots[row - 3][col + 3] == checker:
                        return True
        else:
            return False