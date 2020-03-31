#Graph class implemented from a existant version found at:
#https://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python

from collections import defaultdict
from interface import display_board, print_final, print_board
from game import convert_direction
from heuristics import *
import heapq

class Node(object):
    #constructor, stores the state it represents and the parent (none by default)
    def __init__(self, state, goal_squares, uses_cost,expandables, parent = None, last_move = None):
        self.__state = state
        self.__parent = parent
        self.__last_move = last_move
        self.__goal_squares = goal_squares
        self.__heuristic = heuristic(self.__state,self.__goal_squares)
        self.__uses_cost = uses_cost
        self.expandables = expandables
    
    def get_state(self):
        return self.__state

    def set_parent(self,parent):
        self.__parent = parent
    
    def get_parent(self):
        return self.__parent

    def get_last_move(self):
        return self.__last_move

    def get_goal_squares(self):
        return self.__goal_squares
    
    def get_uses_cost(self):
        return self.__uses_cost
    
    def get_heuristic(self):
        return self.__heuristic

    def get_cost(self):
        if self.__parent == None:
            return 0
        else:
            return self.__parent.get_cost()+1
    
    def __lt__(self, other):
        if self.__uses_cost:
            return (self.__heuristic + self.get_cost()) < (other.get_heuristic() + other.get_cost())
        else:
            return (self.__heuristic) < (other.get_heuristic())

#graph class for directed graphs
class Graph(object):
    #constructor, stores the validation function and add edges function names
    def __init__(self, is_solution, add_edges, goal_squares,informed):
        self.graph = defaultdict(set)
        self.is_solution = is_solution
        self.add_edges = add_edges
        self.goal_squares = goal_squares
        self.informed = informed

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
                print_final(node.get_state(),last_move[0],last_move[1],convert_direction(last_move[2]))
            
    #function to iterate the graph and find a solution 
    #given the start node and searching algorithm function
    def __run_graph(self, start, algorithm,limit):
        
        
        visited = defaultdict(bool)
        queue = [start]
        if self.informed:
            heapq.heapify(queue)
        visited[start] = True
        finished = False

        if self.is_solution(start,self.goal_squares):
            finished = True
            #self.print_path(start)
        while not finished:

            count += 1
            if self.informed:
                node = heapq.heappop(queue)
            else:
                node = queue.pop(0)
            
            #testing
            #display_board(node.get_state(),len(node.get_state()))
            #print("Cost: " + str(node.get_cost()) + "  " + "Heuristic: " + str(node.get_heuristic()))
            #print("Total node cost: " + str(node.get_cost() + node.get_heuristic()))
            #input()
            if limit <= 0:
                return False
            else:
                limit -=1

            for adjacent in self.add_edges(node,self.goal_squares):
                self.add_edge(node,adjacent)


            for adjacent in self.graph[node]:
                if self.is_solution(adjacent,self.goal_squares):
                    adjacent.set_parent(node)
                    finished = True
                    #self.print_path(adjacent)
                    return True
                elif not visited[adjacent]:

                    adjacent.set_parent(node)
                    algorithm(adjacent,queue,visited,limit)

           
            
    @staticmethod
    def __bfs(node, queue, visited, _):
        queue.append(node)
        visited[node] = True
    
    @staticmethod
    def __informed_search(node, queue, visited, _):
        heapq.heappush(queue,node)
        visited[node] = True

    @staticmethod
    def __dfs(node, queue, visited, _):
        queue.insert(0,node)
        visited[node] = True

    def dfs(self,start):
        self.__run_graph(start, self.__dfs,0)
        
    def ids(self,start):
        start_node = copy.deepcopy(start)
        for x in range(5000):
            if self.__run_graph(start_node, self.__dfs,x):
                break
            start_node = copy.deepcopy(start)

    def bfs(self,start):
        self.__run_graph(start, self.__bfs,0)

    def informed_search(self,start):
        self.__run_graph(start, self.__informed_search,0)


