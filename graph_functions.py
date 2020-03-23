from game import verify_game_state,validate_move,execute_move,Direction
from graph import Graph, Node

def is_solution(node):
    state = node.get_state()
    return verify_game_state(state[0],state[1])

#get all boards resultant from moving in every direction
def get_all_moves(boards, board, row, col):
    move_top = board
    move_bottom = board
    move_left = board
    move_right = board

    execute_move(move_top,(row,col,Direction.top.value))
    execute_move(move_bottom,(row,col,Direction.bottom.value))
    execute_move(move_left,(row,col,Direction.left.value))
    execute_move(move_right,(row,col,Direction.right.value))
    
    boards.append(move_top)
    boards.append(move_bottom)
    boards.append(move_left)
    boards.append(move_right)

def get_all_nodes(node):
    state = node.get_state()
    board = state[0]
    goalsquares = state[1]

    nodes = []

    #from the current board, retrieve all boards possible from there
    boards = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                get_all_moves(boards,board,i,j)

    #create node for each board possible (each state)
    for board_state in boards:
        nodes.append(Node((board_state,goalsquares),None))
    for node in nodes:
        print(node)

    print("\n")
    return nodes


#TESTING
########################################################
GameBoard2 = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 2, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 3, 0],
             [0, 0, -2, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]


GoalSquares = [[2, 6]]

options = {
    "bfs": lambda graph: graph.bfs(Node((GameBoard2,GoalSquares),None))
}

options["bfs"](Graph(is_solution,get_all_nodes))