#Graph class implemented from a existant version found at:
#https://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python

from collections import defaultdict
from interface import display_board, print_board_2, print_board
from game import convert_direction
from heuristics import *
import heapq

class Node(object):
    #constructor, stores the state it represents and the parent (none by default)
    def __init__(self, state, goal_squares, parent = None, last_move = None):
        self.__state = state
        self.__parent = parent
        self.__last_move = last_move
        self.__goal_squares = goal_squares
        self.heuristic = heuristic
    
    def get_state(self):
        return self.__state

    def set_parent(self,parent):
        self.__parent = parent
    
    def get_parent(self):
        return self.__parent

    def get_last_move(self):
        return self.__last_move
    
    def __lt__(self, other):
        return self.heuristic(self.__state,self.__goal_squares) < self.heuristic(other.get_state(),self.__goal_squares)


#graph class for directed graphs
class Graph(object):
    #constructor, stores the validation function and add edges function names
    def __init__(self, is_solution, add_edges, goal_squares):
        self.graph = defaultdict(set)
        self.is_solution = is_solution
        self.add_edges = add_edges
        self.goal_squares = goal_squares

    #function to add an edge from node1 to node2
    def add_edge(self, node1, node2):
        self.graph[node1].add(node2)

    def print_path(self, end):
        path = [end]
        parent = end.get_parent()
        while(parent is not None):
            path.insert(0,parent)
            parent = parent.get_parent()
        for node in path:
            last_move = node.get_last_move()
            if last_move != None:
                print_board_2(node.get_state(),last_move[0],last_move[1],convert_direction(last_move[2]))
            
    #function to iterate the graph and find a solution 
    #given the start node and searching algorithm function
    def __run_graph(self, start, algorithm):
        
        initial_limit = 2
        limit = initial_limit
        n_tries = 0

        visited = defaultdict(bool)
        queue = [start]
        #heapq.heapify(queue)
        visited[start] = True
        cost = 0
        finished = False

        if self.is_solution(start,self.goal_squares):
            finished = True
            self.print_path(start)
        while not finished:

            node = queue.pop(0)
            #node = heapq.heappop(queue)
            for adjacent in self.add_edges(node,self.goal_squares):
                self.add_edge(node,adjacent)
        
            for adjacent in self.graph[node]:
                if self.is_solution(adjacent,self.goal_squares):
                    adjacent.set_parent(node)
                    finished = True
                    self.print_path(adjacent)
                elif not visited[adjacent]:
                    adjacent.set_parent(node)
                    algorithm(adjacent,queue,visited,cost,limit,n_tries,finished)
            cost +=1

            if limit <= 0:
                limit = initial_limit
                n_tries +=1
            else:
                limit -=1
               

            
    @staticmethod
    def __bfs(node, queue, visited, _,__,___,_____):
        queue.append(node)
        visited[node] = True
    
    @staticmethod
    def __greedy(node, queue, visited, _):
        heapq.heappush(queue,node)
        visited[node] = True

    @staticmethod
    def __dfs(node, queue, visited, _,__,___,_____):
        queue.insert(0,node)
        visited[node] = True

    @staticmethod
    def __ids(node, queue, visited, _,limit,n_tries,finished):
        if limit == 0:
            queue.append(node)
        else:
            queue.insert(0,node)

        if n_tries > 10: 
            finished = True

        visited[node] = True
        
    def dfs(self,start):
        self.__run_graph(start, self.__dfs)
        
    def ids(self,start):
        self.__run_graph(start, self.__ids)

    def bfs(self,start):
        self.__run_graph(start, self.__bfs)

    def greedy(self,start):
        self.__run_graph(start, self.__greedy)

    def __print_path(self, end):
        path = [end]
        parent = end.get_parent()
        while(parent is not None):
            path.insert(0,parent)
            parent = parent.get_parent()
        for node in path:
            print_board(node.get_state())

