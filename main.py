from tictactoe import TicTacToe
import random
board = TicTacToe()

print("(1)Random\n(2)Alpha Beta Pruning\nSelect Level: ", end=" ")
level = int(input())
board.display_board()

if level == 1: # Level (1) Random
    while not (board.check_user() or board.check_cpu()):
            # User's turn
        print('\nYour turn: \n(row): ', end= " ")
        row = int(input())
        print('(column): ', end= " ")
        column = int(input())

        board.update_user(row, column)
        board.display_board()
           
            # Computer's turn
        row = random.randint(0,2)
        column = random.randint(0,2)
        board.update_cpu(row,column)

        print("\nCPU's turn (row,column): ({},{})".format(column, row))
        board.display_board()

if level == 2: # Level (2) Alpha-Beta Pruning
    while not (board.check_user() or board.check_cpu()):
            # User's turn
        print('(row): ', end= " ")
        row = int(input())
        print('(column): ', end= " ")
        column = int(input())
        
        board.update_user(row, column)
        board.display_board() 

            #TODO Computer's turn
            