from game import goal_squares
from graph import Graph, Node
from graph_functions import is_solution,get_all_nodes
from boards import *
import time
import heapq
# TESTING
#######################################################

test_board = GameBoard3
goal_squares_test = goal_squares(test_board)

options = {
    "bfs": lambda graph: graph.bfs(Node(test_board,goal_squares_test,False)),
    "greedy": lambda graph: graph.informed_search(Node(test_board,goal_squares_test,False)),
    "a*": lambda graph: graph.informed_search(Node(test_board,goal_squares_test,True))
}

#start = time.time()
#options["bfs"](Graph(is_solution,get_all_nodes,goal_squares_test,False))
#end = time.time()
#print("bfs time: " + str(end - start))
start = time.time()
options["greedy"](Graph(is_solution,get_all_nodes,goal_squares_test,False))
end = time.time()
print("greedy time: " + str(end - start))
start = time.time()
options["a*"](Graph(is_solution,get_all_nodes,goal_squares_test,True))
end = time.time()
print("a* time: " + str(end - start))
