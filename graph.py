#Graph class implemented from a existant version found at:
#https://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python

from collections import defaultdict

class Node(object):
    #constructor, stores the state it represents and the parent (none by default)
    def __init__(self, state, parent = None):
        self.__state = state
        self.__parent = parent
    
    def get_state(self):
        return self.__state

    def set_parent(self,parent):
        self.__parent = parent
    
    def get_parent(self):
        return self.__parent


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

    #function to iterate the graph and find a solution 
    #given the start node and searching algorithm function
    def __run_graph(self, start, algorithm):
        
        visited = defaultdict(bool)
        queue = [start]
        visited[start] = True
        cost = 0
        finished = False
        while not finished:
            
            node = queue.pop(0)

            for adjacent in self.add_edges(node):
                self.add_edge(node,adjacent)
        
            for adjacent in self.graph[node]:
                if self.is_solution(adjacent,self.goal_squares):
                    finished = True
                    self.print_path(node)
                elif not visited[adjacent]:
                    adjacent.set_parent(node)
                    algorithm(adjacent,queue,visited,cost)
            cost +=1

    @staticmethod
    def __bfs(node, queue, visited, _):
        queue.append(node)
        visited[node] = True

    def bfs(self,start):
        self.__run_graph(start, self.__bfs)

    def __print_path(self, end):
        path = [end]
        parent = end.get_parent()
        while(parent is not None):
            path.insert(0,parent)
            parent.get_parent()
        for node in path:
            print(node.get_state())