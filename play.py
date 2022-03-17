import curses
import time
from random import randint
from curses import wrapper
from curses.textpad import rectangle
from main import *
from config import *



class View:
    def __init__(self):
        self.mode = SINGLE
        self.game = Game()
        self.displayBoard = None
        self.onOff = False
        self.stdscr = None
        self.prevBlink = (0,0)
    def start(self, stdscr):
        """ Game starts here"""
        if os.get_terminal_size().lines < TERMINAL_SIZE_REQUIREMENTS[0] or os.get_terminal_size().columns < TERMINAL_SIZE_REQUIREMENTS[1]:
            print(os.get_terminal_size())
            print("Please resize your terminal window to a larger size and try again.")
            exit()

        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_RED)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        self.BLUE_AND_YELLOW = curses.color_pair(1)
        self.GREEN_AND_RED = curses.color_pair(2)
        self.RED = curses.color_pair(3)
        stdscr.refresh()

        # temp = curses.newwin(50, 50, 1, 1)
        # temp.addstr(5,5, "hello", self.RED)
        # temp.refresh()
        # temp.addstr(5,5, "boyzzz", self.RED)
        # temp.refresh()
        # stdscr.getch()

        self.stdscr = stdscr
        self.startScreen()
        self.mode = self.playerPrompt()
        self.playContext()
        self.shuffleBoardAnimation()
        self.printBoard()
        self.playPuzzle()

    def startScreen(self):
        """ Start screen animation"""
        self.stdscr.nodelay(True)    
        pad = curses.newpad(1, 100)
        self.stdscr.refresh()
        pad.addstr("Welcome to the Nearly Impossible Chessboard Puzzle")

        for i in range(50):
            try:
                self.stdscr.getch()
                break
            except:
                pass
            self.stdscr.clear()
            self.stdscr.refresh()
            pad.refresh(0, 0, 5, 5, 6, 10 + i)
            time.sleep(0.1)

        pad.refresh(0, 0, 5, 5, 6, 60)
        self.stdscr.getch()

    def playerPrompt(self):
        """
        Prompts player what mode they want to play, current their choice doesnt matter as we are only
        implementing solo player.
        """
        self.stdscr.refresh()  
        
        self.stdscr.nodelay(True)
        side = RIGHT
        while True:
            try:
                key = self.stdscr.getch()
            except:
                key = None
                continue
            if key == curses.KEY_LEFT:
                side = LEFT
            elif key == curses.KEY_RIGHT:
                side = RIGHT
            elif key == curses.KEY_ENTER or key == 10 or key == 13:
                return side
            else:
                continue
            self.stdscr.clear()
            if side == LEFT:
                self.stdscr.addstr(5, 10, "Single Player", self.BLUE_AND_YELLOW | curses.A_BOLD)
                self.stdscr.addstr("|")    
                self.stdscr.addstr("Multi Player")
            else:
                self.stdscr.addstr(5, 10, "Single Player")
                self.stdscr.addstr("|")    
                self.stdscr.addstr("Multi Player", self.BLUE_AND_YELLOW | curses.A_BOLD)
            self.stdscr.refresh()

    def playContext(self):
        """
        Plays the context animation
        """
        self.stdscr.clear()
        pad = curses.newpad(9, 95)
        pad.addstr(CONTEXT_SINGLE_PLAYER1)

        for i in range(10):
            try:
                self.stdscr.getkey()
                break
            except:
                pass
            self.stdscr.clear()
            self.stdscr.refresh()
            pad.refresh(0, 0, 5, 5, 6 + i, 10+i*9)
            time.sleep(0.1)
        self.stdscr.clear()
        self.stdscr.refresh()
        dungeon_image = curses.newwin(21, 30, 15, 25)
        for line in DUNGEON_IMAGE.split("\n"):
            dungeon_image.addstr(line + "\n", self.RED)
        dungeon_image.addstr("Press any key to continue", self.RED)
        dungeon_image.refresh()
        pad.refresh(0, 0, 5, 5, 15, 100)
        self.stdscr.nodelay(False)    
        self.stdscr.getch()

    def printBoard(self):
        """
        Call to print the board.
        """
        self.stdscr.clear()
        rectangle(self.stdscr, CHESSBOARD_Y-2,CHESSBOARD_X-2, CHESSBOARD_Y-2+11, CHESSBOARD_X-2+28)
        self.stdscr.refresh()
        board = self.game.getChessBoard().getBoard()
        if not self.displayBoard:
            self.displayBoard = curses.newwin(9, 26, CHESSBOARD_Y, CHESSBOARD_X)
        self.displayBoard.clear()
        for row in board:
            for val in row:
                if val:
                    self.displayBoard.addstr(" H ")
                else:
                    self.displayBoard.addstr(" T ")
            self.displayBoard.addch("\n")
        self.displayBoard.refresh()

    def shuffleBoardAnimation(self):
        self.stdscr.clear()
        rectangle(self.stdscr, CHESSBOARD_Y-2,CHESSBOARD_X-2, CHESSBOARD_Y-2+11, CHESSBOARD_X-2+28)
        self.stdscr.refresh()
        self.board = self.game.getChessBoard().getBoard()
        if not self.displayBoard:
            self.displayBoard = curses.newwin(9, 26, CHESSBOARD_Y, CHESSBOARD_X)
        for i in range(15):
            self.displayBoard.clear()
            for row in self.board:
                for _ in row:
                    if randint(0, 1):
                        self.displayBoard.addstr(" H ")
                    else:
                        self.displayBoard.addstr(" T ")
                self.displayBoard.addch("\n")
            self.displayBoard.refresh()
            time.sleep(0.1)
    
    def playPuzzle(self):
        self.stdscr.nodelay(True)
        row, col = 0, 0
        self.stdscr.refresh()
        prevTime = time.time()
        while True:
            try:
                key = self.stdscr.getch()
            except:
                key = None
            if key == curses.KEY_LEFT:
                col -= 1
            elif key == curses.KEY_RIGHT:
                col += 1
            elif key == curses.KEY_UP:
                row -= 1
            elif key == curses.KEY_DOWN:
                row += 1
            elif key == curses.KEY_ENTER or key == 10 or key == 13:
                pass
            elif key == 27:
                exit()
            if col > 7:
                col = 7
            elif col < 0:
                col = 0
            if row > 7:
                row = 7
            elif row < 0:
                row = 0


            if time.time() - prevTime > 0.1:
                self.blink(row, col)
                prevTime = time.time()


    def blink(self, row, col):
        """ Blinks a certain position on chessboard"""
        prevLine = self.prevBlink[0]
        prevCol = self.prevBlink[1]
        if prevLine != row or prevCol != col:
            temp = "H" if self.board[prevLine][prevCol] else "T"
            self.displayBoard.addstr(self.prevBlink[0], self.prevBlink[1] * 3 + 1, temp)

        if self.onOff:
            self.displayBoard.addstr(row, col*3 + 1, " ")
            self.displayBoard.refresh()
        else:
            temp = "H" if self.board[row][col] else "T"
            self.displayBoard.addstr(row, col*3 + 1, temp)
            self.displayBoard.refresh()
        self.onOff = not self.onOff
        self.prevBlink = (row, col)

def main():
    view = View()
    wrapper(view.start)
            

if __name__ == "__main__":
    main()