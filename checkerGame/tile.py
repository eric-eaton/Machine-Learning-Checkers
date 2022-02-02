"""
This module creates the tile object which will populate the board object
"""
from piece import CheckerPiece

class Tile:

    def __init__(self):
        self.valid = True
        self.position = ('A', 1)
        self.occupied = False
        self.occupiedPiece = None

    """
    SETTERS
    This block of code is for all the setters for each tile object. 
    There will be a total of 32 unique tile objects created by the board class.
    """

    # set_valid() uses self.postion to assign validity to the tile
    def set_valid(self):
        coor = self.get_position()
        if coor[0] == 'A':
            match coor[1]:
                case 1: self.valid = True
                case 2: self.valid = False
                case 3: self.valid = True
                case 4: self.valid = False
                case 5: self.valid = True
                case 6: self.valid = False
                case 7: self.valid = True
                case 8: self.valid = False

        if coor[0] == 'B':
            match self.position[1]:
                case 1: self.valid = False
                case 2: self.valid = True
                case 3: self.valid = False
                case 4: self.valid = True
                case 5: self.valid = False
                case 6: self.valid = True
                case 7: self.valid = False
                case 8: self.valid = True

        if self.position[0] == 'C':
            match self.position[1]:
                case 1: self.valid = True
                case 2: self.valid = False
                case 3: self.valid = True
                case 4: self.valid = False
                case 5: self.valid = True
                case 6: self.valid = False
                case 7: self.valid = True
                case 8: self.valid = False

        if self.position[0] == 'D':
            match self.position[1]:
                case 1: self.valid = False
                case 2: self.valid = True
                case 3: self.valid = False
                case 4: self.valid = True
                case 5: self.valid = False
                case 6: self.valid = True
                case 7: self.valid = False
                case 8: self.valid = True

        if self.position[0] == 'E':
            match self.position[1]:
                case 1: self.valid = True
                case 2: self.valid = False
                case 3: self.valid = True
                case 4: self.valid = False
                case 5: self.valid = True
                case 6: self.valid = False
                case 7: self.valid = True
                case 8: self.valid = False

        if self.position[0] == 'F':
            match self.position[1]:
                case 1: self.valid = False
                case 2: self.valid = True
                case 3: self.valid = False
                case 4: self.valid = True
                case 5: self.valid = False
                case 6: self.valid = True
                case 7: self.valid = False
                case 8: self.valid = True

        if self.position[0] == 'G':
            match self.position[1]:
                case 1: self.valid = True
                case 2: self.valid = False
                case 3: self.valid = True
                case 4: self.valid = False
                case 5: self.valid = True
                case 6: self.valid = False
                case 7: self.valid = True
                case 8: self.valid = False

        if self.position[0] == 'H':
            match self.position[1]:
                case 1: self.valid = False
                case 2: self.valid = True
                case 3: self.valid = False
                case 4: self.valid = True
                case 5: self.valid = False
                case 6: self.valid = True
                case 7: self.valid = False
                case 8: self.valid = True


    # creates a new piece object.
    def occupy(self, color, label):
        self.occupiedPiece = CheckerPiece(color,self.position,label)
        self.occupied = True


    """ 
    set_positive take the column and row index values from the current iteration of the array
    and then based on the column values creates the coordinate tuple
    so 0,0 would be ('A',1)
    """
    def set_position(self, x_coor, y_coor):
        match x_coor:
            case 0:
                coor = ('A', y_coor)
            case 1:
                coor = ('B', y_coor)
            case 2:
                coor = ('C', y_coor)
            case 3:
                coor = ('D', y_coor)
            case 4:
                coor = ('E', y_coor)
            case 5:
                coor = ('F', y_coor)
            case 6:
                coor = ('G', y_coor)
            case 7:
                coor = ('H', y_coor)

        self.position = coor

    """
    GETTERS
    This block of code is for all getters for each tile object. This will allow the players to know the state of
    all tiles on the board
    """

    def get_valid(self):
        return self.valid

    def get_occupied(self):
        return self.occupied

    def get_position(self):
        return self.position
