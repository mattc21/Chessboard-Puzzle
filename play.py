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
    def start(self):
        if os.get_terminal_size().lines < TERMINAL_SIZE_REQUIREMENTS[0] or os.get_terminal_size().columns < TERMINAL_SIZE_REQUIREMENTS[1]:
            print(os.get_terminal_size())
            print("Please resize your terminal window to a larger size and try again.")
            exit()
        
        wrapper(self.startScreen)
        self.mode = wrapper(self.playerPrompt)
        wrapper(self.playContext)
        wrapper(self.shuffleBoardAnimation)
        wrapper(self.printBoard)
        wrapper(self.playPuzzle)

    def startScreen(self, stdscr):
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_RED)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        self.BLUE_AND_YELLOW = curses.color_pair(1)
        self.GREEN_AND_RED = curses.color_pair(2)
        self.RED = curses.color_pair(3)
        stdscr.nodelay(True)    
        pad = curses.newpad(1, 100)
        stdscr.refresh()
        pad.addstr("Welcome to the Nearly Impossible Chessboard Puzzle")

        for i in range(50):
            try:
                stdscr.getkey()
                return
            except:
                pass
            stdscr.clear()
            stdscr.refresh()
            pad.refresh(0, 0, 5, 5, 6, 10 + i)
            time.sleep(0.1)
        stdscr.getch()

    def playerPrompt(self, stdscr):
        stdscr.refresh()  
        
        stdscr.nodelay(True)
        side = RIGHT
        while True:
            try:
                key = stdscr.getch()
            except:
                key = None
            if key == curses.KEY_LEFT:
                side = LEFT
            if key == curses.KEY_RIGHT:
                side = RIGHT
            if key == curses.KEY_ENTER or key == 10 or key == 13:
                return side
            stdscr.clear()
            if side == LEFT:
                stdscr.addstr(5, 10, "Single Player", self.BLUE_AND_YELLOW | curses.A_BOLD | curses.A_BLINK)
                stdscr.addstr("|")    
                stdscr.addstr("Multi Player")
            else:
                stdscr.addstr(5, 10, "Single Player")
                stdscr.addstr("|")    
                stdscr.addstr("Multi Player", self.BLUE_AND_YELLOW | curses.A_BOLD | curses.A_BLINK)
            stdscr.refresh()

    def playContext(self, stdscr):

        stdscr.clear()

        pad = curses.newpad(9, 95)

        pad.addstr(CONTEXT_SINGLE_PLAYER1)

        for i in range(10):
            try:
                stdscr.getkey()
                break
            except:
                pass
            stdscr.clear()
            stdscr.refresh()
            pad.refresh(0, 0, 5, 5, 6 + i, 10+i*9)
            time.sleep(0.1)
        stdscr.clear()
        stdscr.refresh()
        dungeon_image = curses.newwin(21, 30, 15, 25)
        for line in DUNGEON_IMAGE.split("\n"):
            dungeon_image.addstr(line + "\n", self.RED)
        dungeon_image.addstr("Press any key to continue", self.RED)
        dungeon_image.refresh()
        pad.refresh(0, 0, 5, 5, 15, 100)
        stdscr.nodelay(False)    
        stdscr.getch()

    def printBoard(self, stdscr):
        stdscr.clear()
        rectangle(stdscr, CHESSBOARD_Y-2,CHESSBOARD_X-2, CHESSBOARD_Y-2+11, CHESSBOARD_X-2+28)
        stdscr.refresh()
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
        stdscr.getch()

    def shuffleBoardAnimation(self, stdscr):
        stdscr.clear()
        rectangle(stdscr, CHESSBOARD_Y-2,CHESSBOARD_X-2, CHESSBOARD_Y-2+11, CHESSBOARD_X-2+28)
        stdscr.refresh()
        board = self.game.getChessBoard().getBoard()
        if not self.displayBoard:
            self.displayBoard = curses.newwin(9, 26, CHESSBOARD_Y, CHESSBOARD_X)
        for i in range(15):
            self.displayBoard.clear()
            for row in board:
                for _ in row:
                    if randint(0, 1):
                        self.displayBoard.addstr(" H ")
                    else:
                        self.displayBoard.addstr(" T ")
                self.displayBoard.addch("\n")
            self.displayBoard.refresh()
            time.sleep(0.1)
    
    def playPuzzle(self, stdscr):
        stdscr.nodelay(True)
        line, row = 0, 0
        while True:
            try:
                key = stdscr.getch()
            except:
                key = None
            if key == curses.KEY_LEFT:
                pass
            elif key == curses.KEY_RIGHT:
                pass
            elif key == curses.KEY_UP:
                pass
            elif key == curses.KEY_DOWN:
                pass
            elif key == curses.KEY_ENTER or key == 10 or key == 13:
                pass

            self.blink(line, row)

    def blink(self, line, row):
        """ Blinks a certain position on chessboard"""
        
        wrapper(self.printBoard)
        if self.onOff:
            self.displayBoard.addstr(CHESSBOARD_Y + 2, CHESSBOARD_X + 2, " ")
            self.displayBoard.refresh()
        self.onOff = not self.onOff

def main():
    view = View()
    view.start()
            

if __name__ == "__main__":
    main()