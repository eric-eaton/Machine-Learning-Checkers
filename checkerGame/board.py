"""
A Checkers board is an 8x8 array. This will be represented by a numpy array. In checkers, a square is either occupied
or unoccupied. This will be represented with NaN values.
"""
import numpy as np
from tile import Tile


class CheckerBoard:


    """
    CONSTRUCTOR
    This constructor creates an empty 8x8 numpy array and then fills it with NaN values.
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
    This function returns the board created by the constructor
    """
    def getBoard(self):
        return self.board
