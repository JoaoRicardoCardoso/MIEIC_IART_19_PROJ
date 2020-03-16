def game(mode,level,search):
    print("mode:")
    print(mode)
    print("level:")
    print(level)
    print("search:")
    print(search)

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
                valid_input = True
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
                valid_input = True
                option = int(option)
                if option == 4:
                    return False
                elif option == 5:
                    return True
                if mode == 1:
                    game(mode,option,-1)
                    return True
                elif mode == 2:
                    if search_menu(mode, option):
                        return True
            else: 
                print("Invalid input. Please select a valid option.")
        else:
            print("Invalid input. Please select a valid option.")     

def search_menu(mode, level):
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
                valid_input = True
                option = int(option)
                if option == 3:
                    return False
                elif option == 4:
                    return True
                else:
                    game(mode,level,option)
                    return True
            else: 
                print("Invalid input. Please select a valid option.")
        else:
            print("Invalid input. Please select a valid option.")     

#-------------------------------------------------------------------
def verify_game_state(board,goalsquares):
    for goal in goalsquares:
        if board[goal[1]][goal[0]] == Piece.filled.value:
            return True
    return False

#TESTING
#print_board(GameBoard)
#print(str(verify_game_state(GameBoard,GoalSquares)))
#needs more boards to test

#-------------------------------------------------------------------
def goal_squares(board):
    goalsquares=[]
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == -2:
                goalsquares.append([col,row])
    return goalsquares
    
#TESTING
#print_board(GameBoard)
#print(str(goal_squares(GameBoard)))
#needs more boards to test
