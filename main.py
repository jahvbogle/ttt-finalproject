from tictactoe import TicTacToe
import random
board = TicTacToe()

print("(1)Random\n(2)Alpha Beta Pruning\nSelect Level: ", end=" ")
level = int(input())

if level == 1: # Level (1) Random
    while not (board.check_user() or board.check_cpu()):
            # User's turn
        print('user_x: ', end= " ")
        user_x = int(input())
        print('user_y: ', end= " ")
        user_y = int(input())
        board.update_user(user_x, user_y)
            
            # Computer's turn (Random)
        random_x = random.randint(0,2)
        random_y = random.randint(0,2)
        board.update_cpu(random_x,random_y)

            # Display current state of board
        current_board = board.get_board()
        for column in current_board:
            print(column)

if level == 2: # Level (2) Alpha-Beta Pruning
    while not (board.check_user() or board.check_cpu()):
            # User's turn
        print('user_x: ', end= " ")
        user_x = int(input())
        print('user_y: ', end= " ")
        user_y = int(input())
        board.update_user(user_x, user_y)
            
            #TODO Computer's turn

            # Display current state of board
        current_board = board.get_board()
        for column in current_board:
            print(column)