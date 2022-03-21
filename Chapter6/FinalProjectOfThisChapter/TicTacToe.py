# Tic-tac-toe
# Computer playing tic-tac-toe against man
   
# Global constants
from queue import Empty
from urllib import response


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

def askYesNo(question):
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response

def askNumber(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    goFirst =askYesNo("Do you want to be entitled to the first move? (t/n):")
    if goFirst == 't':
        print("So the first move is yours, you'll need it.")
        human = X
        computer = O
    else:
        print("Your courage will get you lost... I make the first move.")
        computer = X
        human = O
    return computer, human

def newBoard():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def displayBoard():
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

