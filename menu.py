from graph import Node, Graph
from game import goal_squares,game
from boards import GameBoard1,GameBoard2,GameBoard3,GameBoard4
from graph_functions import is_solution, get_all_nodes

def main_menu():
    while True:
        print()
        print("---------Zhed Solver---------")
        print()
        print("Mode selection:")
        print("1- Human")
        print("2- Computer")
        print("3- Exit")
        print()

        option = input("Choose an option: ")
        if len(option) == 1:
            if ord(option) >= 49 and ord(option) <= 51:
                option = int(option)
                if option == 3:
                    return
                if level_menu(option):
                    return
            else:
                print("Invalid input. Please select a valid option.")
        else:
            print("Invalid input. Please select a valid option.")


def level_menu(mode):
    while True:
        if mode == 1:
            print()
            print("----------Human Mode----------")
            print()
        elif mode == 2:
            print()
            print("---------Computer Mode---------")
            print()

        print("Level selection:")
        print("1- Level 1")
        print("2- Level 2")
        print("3- Level 3")
        print("4- Back")
        print("5- Exit")

        option = input("Choose an option: ")
        if len(option) == 1:
            if ord(option) >= 49 and ord(option) <= 53:
                option = int(option)
                if option == 4:
                    return False
                elif option == 5:
                    return True
                if mode == 1:
                    game(mode, option, -1)
                    return True
                elif mode == 2:
                    if search_menu(mode, option):
                        return True
            else:
                print("Invalid input. Please select a valid option.")
        else:
            print("Invalid input. Please select a valid option.")

def switch_level(argument):
    switcher = {
        1: GameBoard1,
        2: GameBoard2,
        3: GameBoard4
    }
    return switcher.get(argument)

def search_menu(mode, level):
    
    board = switch_level(level)

    while True:

        print()
        print("----------Computer Mode----------")
        print()
        print("Search type selection:")
        print("1- Blind Search")
        print("2- Heuristic Search")
        print("3- Back")
        print("4- Exit")

        option = input("Choose an option: ")
        if len(option) == 1:
            if ord(option) >= 49 and ord(option) <= 52:
                option = int(option)
                if option == 3:
                    return False
                elif option == 4:
                    return True
                else:
                    if mode == 2:
                        goalSquares = goal_squares(board)
                        options = {
                                "bfs": lambda graph: graph.bfs(Node(board,goalSquares,False)),
                                "dfs": lambda graph: graph.dfs(Node(board,goalSquares,False)),
                                "ids": lambda graph: graph.ids(Node(board,goalSquares,False)),
                                "greedy": lambda graph: graph.informed_search(Node(board,goalSquares,False)),
                                "a*": lambda graph: graph.informed_search(Node(board,goalSquares,True))
                        }
                        options["greedy"](Graph(is_solution, get_all_nodes, goalSquares))
                    elif mode == 1:
                        game(mode, board, option)
                    return True
            else: 
                print("Invalid input. Please select a valid option.")
        else:
            print("Invalid input. Please select a valid option.")     

main_menu()
