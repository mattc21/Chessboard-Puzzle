from config import *
from random import randint


class Chessboard:
    def __init__(self):
        self.size = BOARDSIZE
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.key = (randint(0, self.size - 1), randint(0, self.size - 1))
    
    def randomiseBoard(self):
        self.board = [[randint(0, 1) for _ in range(self.size)] for _ in range(self.size)]
        
    def placeKey(self, row, col):
        self.key = (row, col)
    
    def flipCoin(self, row, col):
        self.board[row][col] ^= 1

    def getBoard(self):
        return self.board

    def getKey(self):
        return self.key
    
    def getSize(self):
        return self.size


    



class Game:
    def __init__(self, maxFlips = MAXFLIPS):
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

    def checkGuess(self, row, col):
        if row == self.chessBoard.getKey()[0] and col == self.chessBoard.getKey()[1]:
            return True
        return False

    def getChessBoard(self):
        return self.chessBoard

    def getKeyEncoding(self):
        row, col = self.chessBoard.getKey()
        return self.getBinaryEncoding(row, col) 

    def getBinaryEncoding(self, row, col):
        return row + (col * self.chessBoard.getSize())
    
    def calculateBoardValue(self):
        """
        We calculate the board value by doing bitwise addition without carry of the binary encoding of each
        position on the board
        """
        ret = 0
        for i, row in enumerate(self.chessBoard.getBoard()):
            for j, value in enumerate(row):
                if value:
                    ret ^= self.getBinaryEncoding(i, j)
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
        for i, row in enumerate(self.chessBoard.getBoard()):
            for j, value in enumerate(row):
                if self.getBinaryEncoding(i, j) == changes:
                    return (i, j)
        
        raise Exception("Something bad occurred in calculateFlipLocation")

    def flipsDone(self):
        return self.flips >= self.maxFlips
