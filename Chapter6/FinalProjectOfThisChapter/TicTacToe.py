# Tic-tac-toe
# Computer playing tic-tac-toe against man
   
# Global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    print(
    """
    Welcome to the greatest intellectual challenge of all time, the
    game of 'Tic-tac-toe'. This will be the ultimate showdown between your
    human brain and my silicon processor.  

    You will indicate your move by entering a number between 0 and 8.
    This number corresponds to the position on the board according to the diagram below:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    Get ready, man.  The final battle is about to begin. \n
    """
    )

