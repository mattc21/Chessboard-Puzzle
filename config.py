import os


HEADS = 1
TAILS = 0
BOARDSIZE = 8
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
MAXFLIPS = 1
HELPMESSAGE = f"""Scenario:
You and your treasure hunter friend are locked in a dungeon. The witch gives you a chance at freedom.
She leads you to a room. Your friend is waiting outside, unable to see or hear. 

In front of you is an {BOARDSIZE} x {BOARDSIZE} chessboard. In a compartment within one of the squares, 
she places the key to escape the dungeon.

She places a coin on top of each square on the chessboard, randomly assigning them heads or tails. 
You know where the key is, but your friend does not. You are given {MAXFLIPS} flip/s to communicate
where the key is hidden to your friend. Then you will be led out the room and your friend will enter
the room. If he does guess correctly where the key is on the first try, you are locked forever in 
the dungeon.

Good luck! You were given a chance to create a strategy with your friend beforehand.
"""

WINMESSAGE = """
THE WITCH CANNOT BELIEVE IT.
YOUR FRIEND CORRECTLY GUESSES THE KEY. YOU ARE FREED.
"""

LOSEMESSAGE = """
THE WITCH IS DELIGHTED TO HAVE NEW COMPANY.
YOU LOSE YOUR CHANCE AT FREEDOM.
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

