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
    number_of_X = 0
    number_of_O = 0

    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column == X:
                number_of_X += 1
            if column == O:
                number_of_O += 1

    if number_of_X == number_of_O:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column != X or column != O:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    i = action[0]
    j = action[1]
    if new_board[i][j] == X or new_board[i][j] == O:
        return Exception
    else:
        if player(board) == X:
            new_board[i][j] = X
        else:
            new_board[i][j] = O
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Three in a row
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == X:
            return X
        elif board[i][0] == board[i][1] == board[i][2] == O:
            return O

    # Three in a column
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == X:
            return X
        elif board[0][j] == board[1][j] == board[2][j] == O:
            return O

    # Diagonal \
    if board[0][0] == board[1][1] == board[2][2] == X:
            return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
            return O

    # Diagonal /
    if board[0][2] == board[1][1] == board[2][0] == X:
            return X
    elif board[0][2] == board[1][1] == board[2][0] == O:
            return O

    # No winners
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if board is full
    def full_board(board):

        number_of_Empty = 0

        for row in board:
            for column in row:
                if column == EMPTY:
                    number_of_Empty += 1

        if number_of_Empty == 0:
            return True
        else:
            return False


    if winner(board) != None:
        return True
    elif full_board(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None


    if board == initial_state():
        return 0, 1

    # If player is X, player will try to maximise value
    if player(board) == X:
        best_value = -math.inf
    # If player is O, player will try to minimise value
    else:
        best_value = math.inf

    for action in actions(board):
        new_value = minimax_value(result(board, action), best_value)

        if player(board) == X:
            new_value = max(best_value, new_value)

        if player(board) == O:
            new_value = min(best_value, new_value)

        if new_value != best_value:
            best_value = new_value
            best_action = action

    return best_action

def minimax_value(board, best_value):
    # If player is X, player will try to maximise value
    if player(board) == X:
        value = -math.inf
    # If player is O, player will try to minimise value
    else:
        value = math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        new_value = minimax_value(result(board, action), value)

        if player(board) == X:
            if new_value > best_value:
                return new_value
            value = max(value, new_value)

        if current_player == O:
            if new_value < best_value:
                return new_value
            value = min(value, new_value)

    return value