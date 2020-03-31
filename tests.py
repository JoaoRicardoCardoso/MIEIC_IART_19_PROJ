from game import get_expandables, goal_squares
from graph import Graph, Node
from graph_functions import is_solution,get_all_nodes
from boards import *
import time
import heapq
import xlsxwriter
# TESTING
#######################################################

test_board = GameBoard2
goal_squares_test = goal_squares(test_board)

options = {
    "bfs": lambda graph: graph.bfs(Node(test_board,goal_squares_test,False,get_expandables(test_board))),
    "dfs": lambda graph: graph.dfs(Node(test_board,goal_squares_test,False,get_expandables(test_board))),
    "ids": lambda graph: graph.ids(Node(test_board,goal_squares_test,False,get_expandables(test_board))),
    "greedy": lambda graph: graph.informed_search(Node(test_board,goal_squares_test,False,get_expandables(test_board))),
    "a*": lambda graph: graph.informed_search(Node(test_board,goal_squares_test,True,get_expandables(test_board)))
}

# start = time.time()
# options["bfs"](Graph(is_solution,get_all_nodes,goal_squares_test,False))
# end = time.time()
# print("bfs time: " + str(end - start))

# start = time.time()
# options["dfs"](Graph(is_solution,get_all_nodes,goal_squares_test,False))
# end = time.time()
# print("dfs time: " + str(end - start))

#start = time.time()
#options["ids"](Graph(is_solution,get_all_nodes,goal_squares_test,False))
#end = time.time()
#print("ids time: " + str(end - start))

# start = time.time()
# options["greedy"](Graph(is_solution,get_all_nodes,goal_squares_test,True))
# end = time.time()
# print("greedy time: " + str(end - start))

# start = time.time()
# options["a*"](Graph(is_solution,get_all_nodes,goal_squares_test,True))
# end = time.time()
# print("a* time: " + str(end - start))

workbook = xlsxwriter.Workbook('ids2.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('D1', 'BFS')
for x in range(1,20):
    start = time.time()
    options["ids"](Graph(is_solution, get_all_nodes, goal_squares_test,False))
    end = time.time()
    print("time: " + str(end - start))
    worksheet.write(x, 2, end - start)
    worksheet.write(x, 3, end - start)
    start = 0
    end = 0
workbook.close()