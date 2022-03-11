from pyexpat.errors import XML_ERROR_UNKNOWN_ENCODING
from config import *
from random import randint
from pygame import *

class Chessboard:
    def __init__(self):
        self.size = BOARDSIZE
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.key = (randint(0, self.size - 1), randint(0, self.size - 1))
    
    def randomiseBoard(self):
        self.board = [[randint(0, 1) for _ in range(self.size)] for _ in range(self.size)]
        
    def placeKey(self, s: str):
        self.key = Chessboard.convertStringToXY(s)
    
    def flipCoin(self, s: str):
        x, y = Chessboard.convertStringToXY(s)
        self.board[x][y] ^= 1

    def getBoard(self):
        return self.board

    def getKey(self):
        return self.key
    
    def getSize(self):
        return self.size

    @staticmethod
    def convertStringToXY(s: str):
        """ Converts a chess position string to an x y coordinate. A typical chess coordinate is A1 """
        
        letter = ord(s[0])
        number = int(s[1:]) - 1

        if letter >= 97 and letter - 97 < BOARDSIZE:
            return (letter- 97, number)
        if letter >= 65 and letter - 65 < BOARDSIZE:
            return (letter- 65, number)
        else:
            raise Exception("Error, chess positions are a letter followed by number")

    @staticmethod   
    def convertXYtoString(x: tuple):
        if len(x) != 2:
            raise Exception("XY is a tuple of length 2")
        
        return str(ALPHABET[x[0]]) + str(x[1]+1)

    
        

class Game:
    def __init__(self, maxFlips = 1):
        self.chessBoard = Chessboard()
        self.chessBoard.randomiseBoard()
        self.flips = 0
        self.maxFlips = maxFlips

    def resetGame(self):
        self.chessBoard.randomiseBoard()

    def flipCoin(self, s: str):
        if self.flips < self.maxFlips:
            self.chessBoard.flipCoin(s)
            self.flips += 1

    def placeKey(self, s: str):
        self.chessBoard.placeKey(s)

    def checkGuess(self, s: str):
        if Chessboard.convertStringToXY(s) == self.chessBoard.getKey():
            return True
        return False

    def getChessBoard(self):
        return self.chessBoard

    def getKeyEncoding(self):
        x, y = self.chessBoard.getKey()
        return self.getBinaryEncoding(x, y) 

    def getBinaryEncoding(self, x, y):
        return x + (y * self.chessBoard.getSize())
    
    def calculateBoardValue(self):
        """
        We calculate the board value by doing bitwise addition without carry of the binary encoding of each
        position on the board
        """
        ret = 0
        for x, row in enumerate(self.chessBoard.getBoard()):
            for y, value in enumerate(row):
                if value:
                    ret ^= self.getBinaryEncoding(x, y)
        # format(ret, '#008b')
        return ret

    def calculateFlipLocation(self):
        """
        We calculate which coin to flip such that board value is         
        """
        size = self.chessBoard.getSize()
        
        # Check if size of board is divisible by 2 using bitwise operation
        if not (size & (size - 1) == 0 and size != 0):
            return (-1, -1)

        numBits = len(bin(size**2 - 1)) - 2
        curr = self.calculateBoardValue()
        desired = self.getKeyEncoding()
        changes = (curr ^ desired) & int("1"*numBits, 2)
        for x, row in enumerate(self.chessBoard.getBoard()):
            for y, value in enumerate(row):
                if self.getBinaryEncoding(x, y) == changes:
                    return (x, y)
        
        raise Exception("Something bad occurred in calculateFlipLocation")