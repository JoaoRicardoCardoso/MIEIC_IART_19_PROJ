from enum import Enum
import re

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

class Direction(Enum):
    top = 0
    right = 1
    bottom = 2
    left = 3
    @classmethod
    def is_direction(cls,dir):
        return dir in cls._value2member_map_

#-------------------------------------------------------------------
# board - matrix of arrays
# move - (row,column,direction)
def execute_move(board,move):
    row = move[0]
    column = move[1]
    direction = move[2]
    value = board[row][column]
    if(value <= 0):
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

#-------------------------------------------------------------------
def display_game():
    
    print('\n')
    print('                 Zhed Game    \n')

    Coordenates = [0,0,1,2,3,4,5,6,'']

    row_format ="{:>4}" * (len(Coordenates) + 1)
    print(row_format.format("y|x", *Coordenates))
    print('   ------------------------------------')

    Coords = []
    for x in Coordenates:
        Coords.append(str(x) +' |')
    
    for value, row in zip(Coords, GameBoard):
        row2 = row + list('|')
        print(row_format.format(value , *row2))
        print('   ------------------------------------')
    

def input_to_direction(value):
    if value == 'R':
        direction = Direction.right
    elif value == 'L':
        direction = Direction.left
    elif value == 'T':
        direction = Direction.top
    elif value == 'B':
        direction = Direction.bottom
    return direction

def create_move(arguments):
    direction = input_to_direction(arguments[2]) 
    return (arguments[0], arguments[1], direction )


def verify_input_number(arg):
    if int(arg) < 10 & int(arg) >= 0:
        return True
    else:
        return False

def verify_input_direction(arg):
    if (arg is "R") or (arg is "L") or (arg is "B") or (arg is "T"):
        return True
    else:
        return False
        
def verify_input(arguments):
    if verify_input_number(arguments[0]) \
        & verify_input_number(arguments[1]) \
        & verify_input_direction(arguments[2]):
        return True
    else:
        return False

def read_move():
    
    while True:
        moveaux = input("What's your play? (Row Column Direction:[L, R, T, B])")
        print(moveaux)
        arguments = moveaux.split()

        leng = len(arguments)
        if leng == 3:
            if verify_input(arguments):
                break
        else:
            print("Incorrect input...Try again \n")
    
    return create_move(arguments)
#display_game()

#-------------------------------------------------------------------
def validate_move(board,move):
    max_row = len(board) - 1
    max_col = len(board[0]) - 1
    mov_row = move[0]
    mov_col = move[1]
    mov_dir = move[2]
    return mov_row >= 0 and mov_row <= max_row \
        and mov_col >= 0 and mov_col <= max_col \
        and board[mov_row][mov_col] > 0 \
        and Direction.is_direction(mov_dir)

#TESTING
# print_board(GameBoard)
# print(str(validate_move(GameBoard,(0,0,0))))
# print(str(validate_move(GameBoard,(20,0,0))))
# print(str(validate_move(GameBoard,(5,6,5))))
# print(str(validate_move(GameBoard,(5,6,1))))
