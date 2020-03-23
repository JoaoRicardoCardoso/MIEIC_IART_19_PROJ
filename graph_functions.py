import graph
import game

def is_solution(node):
    state = node.get_state()
    return verify_game_state(state[0],state[1])

def get_all_nodes(node):
    state = node.get_state()
    board = state[0]
    nodes = []

    #for the node given, retrieve all nodes reachable from this one
    #validate_move
    #execute_move
    #create node

    return nodes

options = {
    "bfs": lambda graph: graph.bfs(((3,3,1),(0,0,0)))
}
