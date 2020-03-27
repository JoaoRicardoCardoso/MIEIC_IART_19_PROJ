from game import goal_squares
from graph import Graph, Node
from graph_functions import is_solution,get_all_nodes
from boards import test1,test2
# TESTING
#######################################################

goal_squares_test = goal_squares(test2)

#   "greedy": lambda graph: graph.greedy(Node(GameBoard2,GoalSquares))
options = {
    "bfs": lambda graph: graph.bfs(Node(test2,goal_squares_test)),
    "greedy": lambda graph: graph.greedy(Node(test2,goal_squares_test))
}

#options["bfs"](Graph(is_solution,get_all_nodes,GoalSquares))
options["greedy"](Graph(is_solution,get_all_nodes,goal_squares_test))