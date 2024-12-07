from tictactoe import TicTacToe
import random
board = TicTacToe()

def user(turn):
    print('\n----------Turn ({})----------\nYour turn: \n(row): '
        .format(turn), end= " ")
    row = int(input())
    print('(column): ', end= " ")
    column = int(input())

    if not board.board[row][column] == ' ':
        print("\nInvalid move (User) (Position occupied: '{}' at row={} column={})"
        .format(board.board[row][column], row, column))
        user(turn)
    else:
        board.update_user(row, column)
        board.display_board()

def random_cpu():
    row = random.randint(0,2)
    column = random.randint(0,2)
    print("\nCPU's turn (row,column): ({},{})"
        .format(row, column))
    
    if not board.board[row][column] == ' ':
        print("Invalid move (CPU) (Position occupied: '{}' at row={} column={})"
        .format(board.board[row][column], row, column))
        random_cpu()
    else:
        board.update_cpu(row, column)
        board.display_board()

print("(1)Random\n(2)Alpha Beta Pruning\nSelect Level: ", end=" ")
level = int(input())
board.display_board()

if level == 1: # Level (1) Random
    turn = 1
    while not (board.check_user() or board.check_cpu()):
        if board.check_tie(): 
            print('\nGame over\nResult: Tie')  
            break
        user(turn) # User's turn

        if board.check_tie(): 
            print('\nGame Over\nResult: Tie')
            break
        random_cpu() # Computer's turn
        turn+=1

if level == 2: # Level (2) Alpha-Beta Pruning
    turn = 1
    while not (board.check_user() or board.check_cpu()):
            # User's turn
            #TODO Computer's turn
        turn+1