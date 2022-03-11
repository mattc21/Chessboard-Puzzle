import os

SINGLE = 0
TWOPLAYER = 1

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
After escaping a treacherous dungeon, you feel bad for the witch who trapped you there as she seems 
to be stuck in the dungeon and rather lonely.

You stupidly leave adventurer friend behind, and head back into the dungeon. Meeting the witch, she
reveals that for her to leave the dungeon, she must solve a puzzle in a special room. However, the 
puzzle requires two people to complete. As such she has been trapped here for a very long time. 
Now you must, with the witch complete the puzzle and save the witch and yourself from eternal 
boredom in the dungeon.
"""

CONTEXT_SINGLE_PLAYER2 = """Gameplay:
One participant must first enter the room. In the room is a {BOARDSIZE} x {BOARDSIZE} chessboard. 
In a compartment within one of the squares is the magic key to escape. Apart starting the game, 
the key will be randomy placed in a compartment within one of the squares of the chessboard. The 
first participant will know where the key is, but the second, waiting outside, will not. 

On top of each of the squares is a coin, randomly flipped heads or tails. The first participant may
flip one coin, after which they are teleported to the waiting room. The second participant enters
immediately after. Using only the coins, the participant must then determine where the key is in
one try. If the participant fails, the duo will be forever trapped in the dungeon!
"""

CONTEXT_SINGLE_PLAYER3A = """Strategy:
The witch decides to go first. She explains a strategy to you. She will assign each position on the
board, a number from 0 to 63. A1 is given the number 0, A2 is given the number 1 and so forth till
H8 is given the number 63.

The code for where the key is will be the number but in binary.

The chessboard state will point to exactly the key location. The state can be calculated by bitwise
addition of each of the squares where the coin has heads facing upwards.

With this strategy, you are now responsible for choosing the correct location.
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

