from game import Direction, execute_move, get_expandables, goal_squares, validate_move, verify_game_state
from graph import Graph, Node
import copy

def is_solution(node, goal_squares):
    state = node.get_state()
    return verify_game_state(state,goal_squares)

#get all newstates resultant from moving in every direction
def get_all_moves(newstates, board, expandable):
    move_top = copy.deepcopy(board)
    move_bottom = copy.deepcopy(board)
    move_left = copy.deepcopy(board)
    move_right = copy.deepcopy(board)

    execute_move(move_top,(expandable[0],expandable[1],Direction.top.value))
    execute_move(move_bottom,(expandable[0],expandable[1],Direction.bottom.value))
    execute_move(move_left,(expandable[0],expandable[1],Direction.left.value))
    execute_move(move_right,(expandable[0],expandable[1],Direction.right.value))
    
    newstates.append((move_top,(expandable[0],expandable[1],Direction.top.value,expandable[2])))
    newstates.append((move_bottom,(expandable[0],expandable[1],Direction.bottom.value,expandable[2])))
    newstates.append((move_left,(expandable[0],expandable[1],Direction.left.value,expandable[2])))
    newstates.append((move_right,(expandable[0],expandable[1],Direction.right.value,expandable[2])))

def get_all_nodes(node,goal_squares):

    board = node.get_state()

    nodes = []
    #from the current board, retrieve all newstates possible from there

    for expandable in node.expandables:
        newstates = []
        get_all_moves(newstates,board,expandable)
        new_expandables = copy.deepcopy(node.expandables)
        new_expandables.remove(expandable)
        for newstate in newstates:
            nodes.append(Node(newstate[0],goal_squares,node.get_uses_cost(),node.get_is_informed(),new_expandables,None,newstate[1]))
    
    return nodes

