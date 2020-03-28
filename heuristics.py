import math as m
import copy

#returns list with all expandable squares
def get_expandables(board):
    expandables = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            value = board[row][col]
            if value > 0:
                expandables.append((row,col,value))
    return expandables

def distance_to_goals(goal_squares,row,col):
    distance = 0.0
    for goal in goal_squares:
        distance = distance + m.sqrt((row-goal[0])*(row-goal[0])+(col-goal[1])*(col-goal[1]))
    return distance

def heuristic1(board,goal_squares):
    expandables = get_expandables(board)
    distances = []

    for expandable in expandables:
        distances.append(distance_to_goals(goal_squares,expandable[0],expandable[1]))
    
    #get the biggest distance (O(n) complexity)
    max = 0
    for distance in distances:
        if distance > max:
            max = distance
    return max #/(m.sqrt(2*len(board)*len(board))) fine tune to make cost more important, probably doesn't make sense

#maximize the amount of possible intersections per expandable square
def heuristic2(board,goal_squares):
    expandables = get_expandables(board)
    intersections = 0
    for expandable in expandables:
        row = expandable[0]
        col = expandable[1]

        value = copy.deepcopy(expandable[2])
        for i in range(1,value+1):
            if col+i >= len(board[0]):
                break
            if board[row][col+i] == -1 or board[row][col+i] > 0:
                intersections += 1

        value = copy.deepcopy(expandable[2])
        for i in range(1,value+1):
            if col-i < 0:
                break
            if board[row][col-i] == -1 or board[row][col-i] > 0:
                intersections += 1

        value = copy.deepcopy(expandable[2])
        for i in range(1,value+1):
            if row+i >= len(board[0]):
                break
            if board[row+i][col] == -1 or board[row+i][col] > 0:
                intersections += 1

        value = copy.deepcopy(expandable[2])
        for i in range(1,value+1):
            if row-i < 0:
                break
            if board[row-i][col] == -1 or board[row-i][col] > 0:
                intersections += 1

    if len(expandables) == 0:
        intersections = 0
    else:
        intersections /= len(expandables)

    if intersections == 0:
        intersections = 4
    else:
        intersections = 1/intersections + 1
    return intersections

heuristic = heuristic2