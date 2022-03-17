import os

SINGLE = True
TWOPLAYER = False
LEFT = True
RIGHT = False
HEADS = 1
TAILS = 0
BOARDSIZE = 8
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
MAXFLIPS = 1
CONTEXT_TWO_PLAYER = f"""Scenario:
You and your treasure hunter friend are locked in a dungeon. The witch gives you a chance at freedom.
She leads you to a room. Your friend is waiting outside, unable to see or hear. 

In front of you is a {BOARDSIZE} x {BOARDSIZE} chessboard. In a compartment within one of the squares, 
she places the key to escape the dungeon.

She places a coin on top of each square on the chessboard, randomly assigning them heads or tails. 
You know where the key is, but your friend does not. You are given {MAXFLIPS} flip/s to communicate
where the key is hidden to your friend. Then you will be led out the room and your friend will enter
the room. If he does guess correctly where the key is on the first try, you are locked forever in 
the dungeon.

Good luck! You were given a chance to create a strategy with your friend beforehand.
"""

CONTEXT_SINGLE_PLAYER1 = """Scenario:
You are stuck in a dungeon with a witch. After a long fight, the witch 
reveals that she too is trapped. This is because she must solve a 
puzzle in a special room. However, the puzzle requires two people 
to complete.

Now you must, with the witch complete the puzzle and save the witch 
and yourself from eternal boredom in the dungeon.
"""

CONTEXT_SINGLE_PLAYER2 = f"""Gameplay:
One participant must first enter the room. In the room is a {BOARDSIZE} 
x {BOARDSIZE} chessboard. In a compartment within one of the squares is 
the magic key to escape. After starting the game, the key will be randomly
 placed in a compartment within one of the squares of the chessboard. The 
first participant will know where the key is, but the second, waiting 
outside, will not. 

On top of each of the squares is a coin, randomly flipped heads or tails. 
The first participant may flip one coin, after which they are teleported 
to the waiting room. The second participant enters immediately after. 
Using only the coins, the participant must then determine where the key is in
one try. If the second participant fails, the duo will be forever trapped 
in the dungeon!
"""

CONTEXT_SINGLE_PLAYER3A = """Strategy:
The witch decides to go first as she is a strong mathematician. She has 
devised a winning strategy. She will assign each position on the
board, a number from 0 to 63. The top-left corner being 0 and the 
bottom-right corner being 63

She will use the chessboard state to point out the key location. The state 
is calculated by bitwise addition without carry of the value of the squares
where the coin has heads facing upwards. Then by converting this binary 
number back to decimal, you will find the key location.
"""

WINMESSAGE_SINGLE = """
YOU FIND THE KEY AND ARE TELEPORTED TO THE WITCH. YOU ESCAPE TO FREEDOM!!
WHATEVER THE WITCH TURNS YOU INTO A FROG...
"""

LOSEMESSAGE_SINGLE = """
YOU SCREW UP...

YOU ARE LOCKED FOREVER WITH THE WITCH. WELL AT LEAST YOU HAVE COMPANY FOR
ALL ETERNITY. MAYBE YOU'LL BE A WIZARD.
"""

WINMESSAGE_TWO = """
THE WITCH CANNOT BELIEVE IT.
YOUR FRIEND CORRECTLY GUESSES THE KEY. YOU ARE FREED.
"""

LOSEMESSAGE_TWO = """
THE WITCH IS DELIGHTED TO HAVE NEW COMPANY.
YOU LOSE YOUR CHANCE AT FREEDOM.
"""

DUNGEON_IMAGE = """__________________________
||          ||          ||
||          ||          ||
||          ||          ||
||          ||          ||
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"""

CHESSBOARD_X = 10
CHESSBOARD_Y = 10

SIDEBOARD_X = 40
SIDEBOARD_Y = 10

TERMINAL_SIZE_REQUIREMENTS = (24, 120)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

