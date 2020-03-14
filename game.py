
GameBoard = [[0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,-1,-1,0,0],
             [0,0,0,-1,-1,-1,0,0],
             [0,0,1,0,0,-1,0,0],
             [0,0,0,0,0,-1,3,0],
             [0,0,-2,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]

GoalSquares = [[2,6]]


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
        


display_game()
