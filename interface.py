import sys
import time
import itertools

def delete_board_screen(n):
    for _ in itertools.repeat(None, 3*n -4):
        sys.stdout.write("\033[F") 
        sys.stdout.write("\033[K") 

def print_move(column,row,direction):
    print("Coordenates: (" + str(column) + "," + str(row) + ")" + " Direction: " + direction)

def print_final(board,column,row,direction):
    print_move(column,row,direction)
    display_board(board,len(board))
    time.sleep(2)
    delete_board_screen(len(board))

def display_board(board,n):

    coordenates = []
    for x in range(0,n):
        coordenates.append(x)
    coordenates.append('')
    print('\n')
    print('                 Zhed Game    \n')

    

    row_format = "{:>4}" * (len(coordenates) + 1)
    print(row_format.format("y|x", *coordenates))
    print('   ', end = '')
    for _ in itertools.repeat(None, n):
        print('----', end = '')
    print('----')


    coords = []
    for x in coordenates:
        coords.append(str(x) + ' |')

    for value, row in zip(coords, board):
        row2 = row + list('|')
        print(row_format.format(value, *row2))
        print('   ', end = '')
        for _ in itertools.repeat(None, n):
            print('----', end = '')
        print('----')



####TESTING#####

def print_board(board):     
    for row in board:
        print("|",end=" ")
        for col in row:
            if col < 0 or col > 10:
                print(col, end=" ")
            else:
                print(" " + str(col),end=" ")
            print("|",end=" ")
        print("")
    print("\n")  