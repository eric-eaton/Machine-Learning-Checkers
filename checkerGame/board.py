"""
A Checkers board is an 8x8 array. This will be represented by a numpy array.
"""
import numpy as np
from tile import Tile


class CheckerBoard:


    """
    CONSTRUCTOR
    This constructor creates an empty 8x8 object numpy array and then fills it with tile objects.
    """
    def __init__(self):
        self.board = np.empty((8, 8),dtype='object')
        self.fill_board()

    def fill_board(self):
        for column in range (0,8):
            for row in range(0,8):
                tile = Tile()
                tile.set_position(column,row+1)
                tile.set_valid()
                self.board[row,column] = tile
    """
    GETTER
    This allows indexing and iteration of the board array object. allows methods contained in the tile class to be
    called by their index postion: board[0,1].get_position() will return ('B',1)
    """
    def __getitem__(self, item):
        return self.board[item]



"""
from board import CheckerBoard
board = CheckerBoard()
"""
