"""
A Checkers board is an 8x8 array. This will be represented by a numpy array. In checkers, a square is either occupied
or unoccupied. This will be represented with NaN values.
"""
import numpy as np

class checkerBoard:
    """
    CONSTRUCTOR
    This constructor creates an empty 8x8 numpy array and then fills it with NaN values.
    """
    def __init__(self):
        self.board = np.empty((8, 8),dtype='object')
    """
    GETTER
    This function returns the board created by the constructor
    """
    def getBoard(self):
        return self.board
