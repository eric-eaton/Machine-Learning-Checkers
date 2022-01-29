"""
Creates a game of checkers
This uses the board.py, pieces.py, and player.py to create the game
"""
from board import checkerBoard
from piece import checkerPieces

class checkerGame:
    def __init__(self):
        self.gameBoard = checkerBoard()
        self.gameBoard = self.gameBoard.getBoard()
        self.pieces = checkerPieces()
        self.red, self.black = self.pieces.getPieceList()



    def fillBoard(self):
        count = 0
        for row in range(0,3):
            if row == 0 or row == 2:
                for column in range(0,7,2):
                    self.gameBoard[row,column] = self.black[count]
                    count+=1
            else:
                for column in range(1,8,2):
                    self.gameBoard[row,column] = self.black[count]
                    count+=1
        count = 0
        for row in range(5,8):
            if row == 6:
                for column in range(0,7,2):
                    self.gameBoard[row,column] = self.red[count]
                    count+=1
            else:
                for column in range(1,8,2):
                    self.gameBoard[row,column] = self.red[count]
                    count+=1



"""from createGame import checkerGame
game = checkerGame()
game.fillBoard()"""