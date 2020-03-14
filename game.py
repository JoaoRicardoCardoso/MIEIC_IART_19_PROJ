from enum import Enum

GameBoard = [[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,-1,-1,0,0],
             [0,0,0,-1,-1,-1,0,0],
             [0,0,1,0,0,-1,0,0],
             [0,0,0,0,0,-1,3,0],
             [0,0,-2,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]


GoalSquares = [[2,6]]

class Piece(Enum):
    empty = 0
    filled = -1
    goal = -2
    @classmethod
    def is_not_expansible(cls,piece):
        return piece in cls._value2member_map_

class Direction(Enum):
    top = 0
    right = 1
    bottom = 2
    left = 3
    @classmethod
    def is_not_direction(cls,dir):
        return dir not in cls._value2member_map_

# board - matrix of arrays
# move - (row,column,direction)
def execute_move(board,move):
    row = move[0]
    column = move[1]
    direction = move[2]
    value = board[row][column]
    if(Piece.is_not_expansible(value)):
        return
    board[row][column] = Piece.filled.value
    if(direction is Direction.top):
        execute_top(board,row,column,value)
    elif(direction is Direction.right):
        execute_right(board,row,column,value)
    elif(direction is Direction.bottom):
        execute_bottom(board,row,column,value)
    elif(direction is Direction.left):
        execute_left(board,row,column,value)

def execute_top(board,row,column,value):
    for i in range(row-1,-1,-1):
        if(value == 0):
            return
        if(board[i][column] is Piece.empty.value 
            or board[i][column] is Piece.goal.value):
            board[i][column] = Piece.filled.value
            value -=1
        
def execute_right(board,row,column,value):
    n_cols = len(board[row])
    for i in range(column+1,n_cols):
        if(value == 0):
            return
        if(board[row][i] is Piece.empty.value 
            or board[row][i] is Piece.goal.value):
            board[row][i] = Piece.filled.value
            value -=1

def execute_bottom(board,row,column,value):
    n_rows = len(board)
    for i in range(row+1,n_rows):
        if(value == 0):
            return
        if(board[i][column] is Piece.empty.value 
            or board[i][column] is Piece.goal.value):
            board[i][column] = Piece.filled.value
            value -=1

def execute_left(board,row,column,value):
    for i in range(column-1,-1,-1):
            if(value == 0):
                return
            if(board[row][i] is Piece.empty.value 
                or board[row][i] is Piece.goal.value):
                board[row][i] = Piece.filled.value
                value -=1

def print_board(board):
    for row in board:
        print(row)
    print('\n')

#TESTING
# print_board(GameBoard)
# execute_move(GameBoard,(5,6,Direction.right))
# print_board(GameBoard)