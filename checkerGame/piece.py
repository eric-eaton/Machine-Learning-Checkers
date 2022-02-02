"""
A checkers game has 24 pieces, 12 black and 12 red.
"""


class CheckerPiece:
    """
    CONSTRUCTOR
    This constructor initializes a checkerPiece object. The constructor takes three arguments, the color, location, and
    label of the piece.
    """
    def __init__ (self, color, location, label):
        self.color = color
        self.location = location
        self.captured = False
        self.king = False
        self.label = label

    """
    PLACEHOLDER
    """
    def move(self,newLocation):
        return newLocation
