import curses
import time
from curses import COLOR_BLUE, COLOR_YELLOW, wrapper
from turtle import right
from config import *




def startScreen(stdscr):
    pad = curses.newpad(1, 100)
    stdscr.refresh()
    pad.addstr("Welcome to the Nearly Impossible Chessboard Puzzle")

    for i in range(50):
        stdscr.clear()
        stdscr.refresh()
        pad.refresh(0, 0, 5, 5, 6, 10 + i)
        time.sleep(0.1)
    stdscr.getch()

def playerPrompt(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_RED)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_RED = curses.color_pair(2)
    pad = curses.newpad(1, 100)
    stdscr.refresh()  
    
    stdscr.nodelay(True)
    side = RIGHT
    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None
        if key == "KEY_LEFT":
            side = LEFT
        if key == "KEY_RIGHT":
            side = RIGHT
        if key == "KEY_ENTER":
            return side
        stdscr.clear()
        if side == LEFT:
            stdscr.addstr(5, 10, "Single Player", BLUE_AND_YELLOW | curses.A_BOLD)
            stdscr.addstr("|")    
            stdscr.addstr("Multi Player")
        else:
            stdscr.addstr(5, 10, "Single Player")
            stdscr.addstr("|")    
            stdscr.addstr("Multi Player", BLUE_AND_YELLOW | curses.A_BOLD)
        stdscr.refresh()

            


wrapper(startScreen)
wrapper(playerPrompt)