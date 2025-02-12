"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xs = 0
    os = 0
    for i in board:
        for j in i:
            if j == "X":
                xs += 1
            elif j == "O":
                os += 1

    
    return "X" if xs <= os else "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    row = 0
    col = 0
    while(row < 3):
        while(col < 3):
            if(board[row][col] == EMPTY):
                moves.append((row, col))
            col += 1
        row += 1
        col = 0
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if(action not in actions(board)):
        raise IndexError
    else:
        newboard = copy.deepcopy(board)

        newboard[action[0]][action[1]] = player(board)

        return newboard




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    row = 0
    col = 0
    while(row < 3):
        while(col < 3):
            if(board[row][col] != EMPTY):
                if(col == 0 and board[row][col] == board[row][col+1] == board[row][col+2]):
                    return board[row][col]
                if(row == 0 and board[row][col] == board[row+1][col] == board[row+2][col]):
                    return board[row][col]
                if(col == 0 and row == 0 and board[row][col] == board[row+1][col+1] == board[row+2][col+2]):
                    return board[row][col]
                if(col == 2 and row == 0 and board[row][col] == board[row+1][col-1] == board[row+2][col-2]):
                    return board[row][col]
            col += 1
        row += 1
        col = 0

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        for i in board:
            for j in i:
                if j == EMPTY:
                    return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    victor = winner(board)
    if victor == "X":
        return 1
    elif victor == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    turn = player(board)
    
    if turn == "X":
        v = -math.inf
    elif turn == "O":
        v = math.inf
    
    optimal = (-1,-1)

    for possibleMoves in actions(board):
        if turn == "X":
            currVal = minValue(result(board, possibleMoves), v)
            if(currVal >= v):
                optimal = possibleMoves
                v = currVal
        elif turn == "O":
            currVal = maxValue(result(board, possibleMoves), v)
            if(currVal <= v):
                optimal = possibleMoves
                v = currVal

    return optimal

#trying to implement alpha beta pruning, if we are giving up, throw away the value variable and make it maxValue(board)
def maxValue(board, value):

    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, minValue(result(board, action), min(v, value)))
        if v <= value:
            return v
    return v

def minValue(board, value):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, maxValue(result(board, action), max(v, value)))
        if v >= value:     #if we have already found the lowest possible maximum
            return v
    return v

    
