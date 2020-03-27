import math as m

def distance_to_goals(goal_squares,row,col):
    distance = 0.0
    for goal in goal_squares:
        distance = distance + m.sqrt((row-goal[0])*(row-goal[0])+(col-goal[1])*(col-goal[1]))
    return distance

def heuristic(board,goal_squares):
    expandables=[]

    #fill list with all expandable squares
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] > 0:
                distance = distance_to_goals(goal_squares,row,col)
                expandables.append((distance,row,col))
    
    #get the biggest distance (O(n) complexity)
    max = 0
    for square in expandables:
        if square[0] > max:
            max = square[0]
    return max