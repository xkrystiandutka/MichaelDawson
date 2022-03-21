# Tic-tac-toe
# Computer playing tic-tac-toe against man
   
# Global constants
from shutil import move


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

def displayBoard(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legalMoves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

def humanMove(board,human):
    legal = legalMoves(board)
    move = None
    while move not in legal:
            move = askNumber("What will your move be? (0 - 8):", 0, NUM_SQUARES)
            if move not in legal:
                print("\nThis field is already occupied, foolish man. Choose another.\n")
    print("Excellent...")
    return move

def computerMove(board, computer, human):
    """Cause the computer to perform the move."""
    # create a working copy, since the function will be changing the list
    board = board[:]
    # best positions to take in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I choose board number", end=" ")
    
    # if the computer can win, make this move
    for move in legalMoves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # this move has been checked, retract it
        board[move] = EMPTY
    
    # if man can win, block this move
    for move in legalMoves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # this move has been checked, retract it
        board[move] = EMPTY

    # since nobody can win in the next move, choose the best free field
    for move in BEST_MOVES:
        if move in legalMoves(board):
            print(move)
            return move
