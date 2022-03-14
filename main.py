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
            raise ValueError("Error, chess positions are a letter followed by number")

    @staticmethod   
    def convertXYtoString(x: tuple):
        if len(x) != 2:
            raise ValueError("XY is a tuple of length 2")
        
        return str(ALPHABET[x[0]]) + str(x[1]+1)

    
        

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

    def flipsDone(self):
        return self.flips >= self.maxFlips

class SimpleView:
    def __init__(self, mode = SINGLE):
        if mode not in (SINGLE, TWOPLAYER):
            raise ValueError("ONLY MODES ARE SINGLE AND TWOPLAYER")
        self.game = Game()
        self.mode = mode
    def printScreen(self):
        clear_screen()
        board = self.game.getChessBoard().getBoard()

        topBar = [str(n) for n in range(1, self.game.getChessBoard().getSize() + 1)]
        temp = "    ".join(topBar)
        print(" -- " + temp)
        for i, row in enumerate(board):
            pRow = ["H" if n else "T" for n in row]
            print(chr(i + 65) + " " + str(pRow))

    def help(self):
        clear_screen()
        if self.mode == SINGLE:
            print(CONTEXT_SINGLE_PLAYER1)
            input("Press any key to continue.")
            clear_screen()
            print(CONTEXT_SINGLE_PLAYER2)
            input("Press any key to continue.")
            clear_screen()
            print(CONTEXT_SINGLE_PLAYER3A)
        else:
            print(CONTEXT_TWO_PLAYER)

        input("Press any key to continue.")




    def processAction(self, s):
        if s in ('H', 'h'):
            self.help()
            self.printScreen()
        elif s in ('F', 'f'):
            square = input("Which square? ")
            try: 
                self.game.flipCoin(square)
                self.printScreen()
                print(square + " flipped")
            except ValueError:
                self.printScreen()
                print("Error. Press F to flip or H for help ")
        else:
            self.printScreen()
            print("Previous command not valid.")

    def simpleGame(self):
        if self.mode == SINGLE:
            self.singlePlayerGame()
        elif self.game == TWOPLAYER:
            self.twoPlayerGame()
        else:
            raise ValueError("Only modes are single player or double player.")
    
    def singlePlayerGame(self):
        temp = Chessboard.convertXYtoString(self.game.calculateFlipLocation())
        self.game.flipCoin(temp)
        
        self.printScreen()
        print("The witch has flipped a coin")
        print("Time to take a guess where the key is...")
        guessMade = False
        while not guessMade:
            guess = input("Make a guess: ")
            if self.checkInputs(guess):
                input("Press any key to continue")
                self.printScreen()
                print("The witch has flipped a coin.")
                print("Time to take a guess where the key is...")
                print("Please enter a valid input.")
                continue
            try:
                self.game.checkGuess(guess)
                guessMade = True
            except ValueError:
                self.printScreen()
                print("The witch has flipped a coin.")
                print("Time to take a guess where the key is...")
                print("Please enter a valid input.")

        clear_screen()
        if self.game.checkGuess(guess):
            print(WINMESSAGE_SINGLE)
        else:
            print(LOSEMESSAGE_SINGLE) 
            print(self.game.getChessBoard().getKey())
    
    def checkInputs(self, s):
        """This checks whether user is asking for helps, hints or candy"""
        if s in ('H', 'h'):
            self.help()
            self.printScreen()
        elif s in ("CHEAT", "Cheat", "cheat"):
            print("You have accessed the secret cheat power")
            print("The board encoding is:" + format(self.game.calculateBoardValue(), '#008b'))
            print("If you can't figure the answer' you're pretty dumb.")
        elif s in ("CANDY", "Candy"):
            print("There is no candy...")
        else:
            return False
        return True

    def twoPlayerGame(self):
        self.printScreen()
        while not self.game.flipsDone():
            print("The key is hidden in " + Chessboard.convertXYtoString(self.game.getChessBoard().getKey()))
            action = input("Enter 'H' for help or 'F' to choose coin to flip. ")
            self.processAction(action)
        
        self.printScreen()
        print("A coin has been flipped. You leave the room and your friend enters.")
        print("Time to take a guess where the key is...")
        
        guessMade = False
        while not guessMade:
            guess = input("Make a guess: ")
            try:
                self.game.checkGuess(guess)
                guessMade = True
            except ValueError:
                self.printScreen()
                print("A coin has been flipped. You leave the room and your friend enters.")
                print("Time to take a guess where the key is...")
                print("Please enter a valid input.")

        clear_screen()
        if self.game.checkGuess(guess):
            print(WINMESSAGE_TWO)
        else:
            print(LOSEMESSAGE_TWO)





if __name__ == "__main__":
    view = SimpleView(SINGLE)
    view.simpleGame()

