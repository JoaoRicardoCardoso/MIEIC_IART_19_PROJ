import math as m
import copy
from game import Direction, Piece, get_expandables
import heapq

def cost1(_,last_move):
    if last_move == None:
        return 0
    else:
        return 1
def cost2(goal_squares,last_move):
    if last_move == None:
        return 0
        
    row = last_move[0]
    col = last_move[1]
    direction = last_move[2]
    value = last_move[3]
    all_costs = []
    heapq.heapify(all_costs)
    for goal_square in goal_squares:
        cost = 0
        if row < goal_square[0] and col < goal_square[1]:
            if direction == Direction.top.value:
                cost = 2
            if direction == Direction.bottom.value:
                cost = 1
            if direction == Direction.right.value:
                cost = 1
            if direction == Direction.left.value:
                cost = 2
        if row < goal_square[0] and col > goal_square[1]:
            if direction == Direction.top.value:
                cost = 2
            if direction == Direction.bottom.value:
                cost = 1
            if direction == Direction.right.value:
                cost = 2
            if direction == Direction.left.value:
                cost = 1
        if row > goal_square[0] and col < goal_square[1]:
            if direction == Direction.top.value:
                cost = 1
            if direction == Direction.bottom.value:
                cost = 2
            if direction == Direction.right.value:
                cost = 1
            if direction == Direction.left.value:
                cost = 2
        if row > goal_square[0] and col > goal_square[1]:
            if direction == Direction.top.value:
                cost = 1
            if direction == Direction.bottom.value:
                cost = 2
            if direction == Direction.right.value:
                cost = 2
            if direction == Direction.left.value:
                cost = 1
        if row < goal_square[0] and col == goal_square[1]:
            if direction == Direction.top.value:
                cost = 3
            if direction == Direction.bottom.value:
                cost = 1
            if direction == Direction.right.value:
                cost = 2
            if direction == Direction.left.value:
                cost = 2
        if row > goal_square[0] and col == goal_square[1]:
            if direction == Direction.top.value:
                cost = 1
            if direction == Direction.bottom.value:
                cost = 3
            if direction == Direction.right.value:
                cost = 2
            if direction == Direction.left.value:
                cost = 2
        if row == goal_square[0] and col < goal_square[1]:
            if direction == Direction.top.value:
                cost = 2
            if direction == Direction.bottom.value:
                cost = 2
            if direction == Direction.right.value:
                cost = 1
            if direction == Direction.left.value:
                cost = 3
        if row == goal_square[0] and col > goal_square[1]:
            if direction == Direction.top.value:
                cost = 2
            if direction == Direction.bottom.value:
                cost = 2
            if direction == Direction.right.value:
                cost = 3
            if direction == Direction.left.value:
                cost = 1
        heapq.heappush(all_costs,cost)
    return heapq.heappop(all_costs)

def distance_to_goals(goal_squares,row,col):
    distance = 0.0
    for goal in goal_squares:
        distance = distance + m.sqrt((row-goal[0])*(row-goal[0])+(col-goal[1])*(col-goal[1]))
    return distance

#minimize the distance from the farthest expandable square to the goal square
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
        value = expandable[2]

        for i in range(1,value+1):
            if col+i >= len(board[0]):
                break
            if board[row][col+i] == Piece.filled.value or board[row][col+i] > 0:
                intersections += 1

        for i in range(1,value+1):
            if col-i < 0:
                break
            if board[row][col-i] == Piece.filled.value or board[row][col-i] > 0:
                intersections += 1

        for i in range(1,value+1):
            if row+i >= len(board[0]):
                break
            if board[row+i][col] == Piece.filled.value or board[row+i][col] > 0:
                intersections += 1

        for i in range(1,value+1):
            if row-i < 0:
                break
            if board[row-i][col] == Piece.filled.value or board[row-i][col] > 0:
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

#minimize the distance from the closest expandable square with a common axis with a goal square and that goal square
def heuristic3(board,goal_squares):
    expandables = get_expandables(board)
    all_minimal_plays = []
    heapq.heapify(all_minimal_plays)
    for expandable in expandables:
        row = expandable[0]
        col = expandable[1]
        value = expandable[2]

        min_plays_expandable = []
        heapq.heapify(min_plays_expandable)
        for goal_square in goal_squares:
            min_plays = 1
            if row == goal_square[0]:
                if col < goal_square[1]:
                    for i in range(col,goal_square[1]):
                        if board[row][i] == Piece.empty.value:
                            min_plays += 1
                elif col > goal_square[1]:
                    for i in range(goal_square[1],col):
                        if board[row][i] == Piece.empty.value:
                            min_plays += 1
                heapq.heappush(min_plays_expandable,min_plays-value)
            elif col == goal_square[1]:
                if row < goal_square[0]:
                    for i in range(row,goal_square[1]):
                        if board[i][col] == Piece.empty.value:
                            min_plays += 1
                elif row > goal_square[0]:
                    for i in range(goal_square[1],row):
                        if board[i][col] == Piece.empty.value:
                            min_plays += 1
                heapq.heappush(min_plays_expandable,min_plays-value)

        if len(min_plays_expandable) > 0:
            heapq.heappush(all_minimal_plays,heapq.heappop(min_plays_expandable))
    if len(all_minimal_plays) > 0:
        return heapq.heappop(all_minimal_plays)
    else:
        return 10

heuristic = heuristic1