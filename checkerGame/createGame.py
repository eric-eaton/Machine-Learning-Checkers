"""
Creates a game of checkers
This uses the board.py, pieces.py, and player.py to create the game
"""
from board import CheckerBoard

class CheckerGame:
    def __init__(self):
        self.gameBoard = CheckerBoard()
        self.fillBoard()

    def fillBoard(self):
        #place black pieces first
        count = 1
        for row in range (0,4):
            for column in range(0,8):
                if self.gameBoard[row,column].get_valid():
                    self.gameBoard[row,column].occupy('black', count)
                    count+=1

        #place red pieces
        count = 1
        for row in range (5,8):
            for column in range(0,8):
                if self.gameBoard[row,column].get_valid():
                    self.gameBoard[row,column].occupy('red', count)
                    count+=1



"""
from createGame import CheckerGame
game = CheckerGame()
"""
