"""
Tic Tac Toe Player
"""
import copy
import math

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
    count_X = count_O = 0
    for row in board:
        for box in row:
            if box == 'X':
                count_X += 1
            elif box == 'O':
                count_O += 1

    if count_X > count_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    row_count = 0
    result_set = set()
    for row in board:
        item_count = 0
        for item in row:
            if item == EMPTY:
                result_set.add((row_count, item_count))
            item_count += 1
        row_count += 1

    return result_set



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action taken!!")
    else:
        row, item = action

        result_board = copy.deepcopy(board)
        result_board[row][item] = player(board)

        return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == X and board[0][1] == X and board[0][2] == X) or (board[1][0] == X and board[1][1] == X and board[1][2] == X) or (board[2][0] == X and board[2][1] == X and board[2][2] == X) or (board[0][0] == X and board[1][0] == X and board[2][0] == X) or (board[0][1] == X and board[1][1] == X and board[2][1] == X) or (board[0][2] == X and board[1][2] == X and board[2][2] == X) or (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    elif (board[0][0] == O and board[0][1] == O and board[0][2] == O) or (board[1][0] == O and board[1][1] == O and board[1][2] == O) or (board[2][0] == O and board[2][1] == O and board[2][2] == O) or (board[0][0] == O and board[1][0] == O and board[2][0] == O) or (board[0][1] == O and board[1][1] == O and board[2][1] == O) or (board[0][2] == O and board[1][2] == O and board[2][2] == O) or (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        flag = 0
        for row in board:
            for item in row:
                if item == EMPTY:
                    flag = 1
                    break
        if flag == 0:
            return True
        else:
            return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)
    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def MaxValue(board):
    v= -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, MinValue(result(board, action)))
    return v

def MinValue(board):
    v= math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, MaxValue(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append((MinValue(result(board, action)),action))
        print(plays)
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]

    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append((MaxValue(result(board, action)),action))
        print(plays)
        return sorted(plays, key=lambda x: x[0])[0][1]