from game import Direction, execute_move, get_expandables, goal_squares, validate_move, verify_game_state
from graph import Graph, Node
import copy

def useless_move(board,expandable,direction,expandables,goal_squares):
    row = expandable[0]
    col = expandable[1]
    value = expandable[2]

    if direction == Direction.top.value:
        for square in expandables+goal_squares:
            if square[0] < row:
                return False
    elif direction == Direction.bottom.value:
        for square in expandables+goal_squares:
            if square[0] > row:
                return False
    elif direction == Direction.left.value:
        for square in expandables+goal_squares:
            if square[0] < col:
                return False
    elif direction == Direction.right.value:
        for square in expandables+goal_squares:
            if square[0] > col:
                return False

    return True

def is_solution(node, goal_squares):
    state = node.get_state()
    return verify_game_state(state,goal_squares)

#get all newstates resultant from moving in every direction
def get_all_moves(newstates, board, expandable,expandables,goal_squares):
    move_top = copy.deepcopy(board)
    move_bottom = copy.deepcopy(board)
    move_left = copy.deepcopy(board)
    move_right = copy.deepcopy(board)

    if not useless_move(move_top,expandable,Direction.top.value,expandables,goal_squares):
        execute_move(move_top,(expandable[0],expandable[1],Direction.top.value))
        newstates.append((move_top,(expandable[0],expandable[1],Direction.top.value,expandable[2])))

    if not useless_move(move_bottom,expandable,Direction.bottom.value,expandables,goal_squares):
        execute_move(move_bottom,(expandable[0],expandable[1],Direction.bottom.value))
        newstates.append((move_bottom,(expandable[0],expandable[1],Direction.bottom.value,expandable[2])))

    if not useless_move(move_left,expandable,Direction.left.value,expandables,goal_squares):
        execute_move(move_left,(expandable[0],expandable[1],Direction.left.value))
        newstates.append((move_left,(expandable[0],expandable[1],Direction.left.value,expandable[2])))
    
    if not useless_move(move_right,expandable,Direction.right.value,expandables,goal_squares):
        execute_move(move_right,(expandable[0],expandable[1],Direction.right.value))
        newstates.append((move_right,(expandable[0],expandable[1],Direction.right.value,expandable[2])))

def get_all_nodes(node,goal_squares):

    board = node.get_state()

    nodes = []
    #from the current board, retrieve all newstates possible from there
    

    for expandable in node.expandables:
        newstates = []
        get_all_moves(newstates,board,expandable,goal_squares,node.expandables)
        new_expandables = copy.deepcopy(node.expandables)
        new_expandables.remove(expandable)
        for newstate in newstates:
            nodes.append(Node(newstate[0],goal_squares,node.get_uses_cost(),new_expandables,None,newstate[1]))
    
    return nodes

