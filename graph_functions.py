from game import Direction, execute_move, goal_squares, validate_move, verify_game_state
from graph import Graph, Node
import copy

def is_solution(node, goal_squares):
    state = node.get_state()
    return verify_game_state(state,goal_squares)

#get all newstates resultant from moving in every direction
def get_all_moves(newstates, board, row, col):
    move_top = copy.deepcopy(board)
    move_bottom = copy.deepcopy(board)
    move_left = copy.deepcopy(board)
    move_right = copy.deepcopy(board)

    execute_move(move_top,(row,col,Direction.top.value))
    execute_move(move_bottom,(row,col,Direction.bottom.value))
    execute_move(move_left,(row,col,Direction.left.value))
    execute_move(move_right,(row,col,Direction.right.value))
    
    newstates.append((move_top,(row,col,Direction.top.value)))
    newstates.append((move_bottom,(row,col,Direction.bottom.value)))
    newstates.append((move_left,(row,col,Direction.left.value)))
    newstates.append((move_right,(row,col,Direction.right.value)))

def get_all_nodes(node,goal_squares):

    board = node.get_state()

    nodes = []
    #from the current board, retrieve all newstates possible from there
    newstates = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                get_all_moves(newstates,board,i,j)

    #create node for each board possible (each state)
    for board_state in newstates:
        nodes.append(Node(board_state[0],goal_squares,None,board_state[1]))
    
    return nodes

