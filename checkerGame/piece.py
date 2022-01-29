"""
A checkers game has 24 pieces, 12 black and 12 red.
"""


class checkerPieces:
    """
    CONSTRUCTOR
    This constructor intializes the red pieces with the character X and the black pieces with the character Y
    It also initializes two lists which will contain the pieces. It then calls fillPieceList() to fill the lists
    """
    def __init__ (self):
        self.redPiece = 'red'
        self.blackPiece = 'black'
        self.redList = []
        self.blackList = []
        self.fillPieceList()

    """
    HELPER
    This function executes 2 for loops which fill each list
    """
    def fillPieceList(self):
        for i in range(0,12):
            self.redList.append(self.redPiece)

        for i in range(0,12):
            self.blackList.append(self.blackPiece)



    def getPieceList(self):
        return self.redList, self.blackList
