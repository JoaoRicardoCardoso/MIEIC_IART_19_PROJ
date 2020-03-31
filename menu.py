from graph import Node, Graph
from game import goal_squares,game,get_expandables
from boards import GameBoard1,GameBoard2,GameBoard3,GameBoard4
from graph_functions import is_solution, get_all_nodes
import time
#import xlsxwriter

def main_menu():
    while True:
        print("\n---------Zhed Solver---------\n")
        print("Mode selection:")
        print("1- Human")
        print("2- Computer")
        print("3- Exit\n")

        try:
            option = input("Choose an option: ")
            option = int(option)
        except ValueError:
            print("Invalid input. Please select a valid option.")
            continue
        if option >= 1 and option <= 3:
            if option < 3:
                return level_menu(option)
            else:
                return
        else:
            print("Invalid input. Please select a valid option.")

def level_menu(mode):
    while True:
        print("\n----------Level Selection----------\n")
        print("Level selection:")
        print("1 - Level 1")
        print("2 - Level 2")
        print("3 - Level 3")
        print("4 - Level 4")
        print("5 - Back")
        print("6 - Exit\n")

        try:
            option = input("Choose an option: ")
            option = int(option)
        except ValueError:
            print("Invalid input. Please select a valid option.")
            continue
        
        if option >=1 and option <= 6:
            if option == 5:
                return False
            elif option == 6:
                return True
            else:
                board = switch_level(option)
                if mode == 1:
                    if game(board):
                        print("\nYou WON!!!")
                    else:
                        print("\nGAME OVER. Next time you'll do better. I hope.")
                else:
                    search_menu(board)
                return True
        else:
            print("Invalid input. Please select a valid option.")

def switch_level(argument):
    switcher = {
        1: GameBoard1,
        2: GameBoard2,
        3: GameBoard3,
        4: GameBoard4
    }
    return switcher.get(argument)

def switch_search_method(option,board,goalSquares):
    expandables = get_expandables(board)
    options = {
        1: lambda graph: graph.bfs(Node(board,goalSquares,False,False,expandables)),
        2: lambda graph: graph.dfs(Node(board,goalSquares,False,False,expandables)),
        3: lambda graph: graph.informed_search(Node(board,goalSquares,False,True,expandables)),
        4: lambda graph: graph.informed_search(Node(board,goalSquares,True,True,expandables))
    }
    return options.get(option)

def search_menu(board):
    while True:    
        print("\n----------Computer Mode----------\n")
        print("Search type selection:")
        print("1 - Breadth First Search")
        print("2 - Depth First Search")
        print("3 - Greedy Search")
        print("4 - A Star")
        print("5 - Back")
        print("6 - Exit\n")

        try:
            option = input("Choose an option: ")
            option = int(option)
        except ValueError:
            print("Invalid input. Please select a valid option.")
            continue
        if option >= 1 and option <= 6:
                if option == 5:
                    return False
                elif option == 6:
                    return True
                else:
                    goalSquares = goal_squares(board)
                    selected = switch_search_method(option,board,goalSquares)
                    start = time.time()
                    selected(Graph(is_solution, get_all_nodes, goalSquares,False))
                    end = time.time()
                    print("Execution time: " + str(round(end - start,5)) + " seconds ")
                    return True
        else:
            print("Invalid input. Please select a valid option.")

main_menu()
