import sys
class TicTacToe:
     def __init__(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        
     def update_user(self, x, y):
        self.board[x][y] = 'X'
        return self.board
     
     def update_cpu(self, x, y):
         self.board[x][y] = 'O'
         return self.board
     
     # Check if goal state is reached
     def check_user(self):
        if ( # Check horizontally
            (self.board[0][0] == 'X' and self.board[0][1] == 'X' and self.board[0][2]) == 'X' or
            (self.board[1][0] == 'X' and self.board[1][1] == 'X' and self.board[1][2]) == 'X' or
            (self.board[2][0] == 'X' and self.board[2][1] == 'X' and self.board[2][2]) == 'X' or

            # Check vertically
            (self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0]) == 'X' or
            (self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1]) == 'X' or
            (self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2]) == 'X' or

            # Check diagonals
            (self.board[0][0]  == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X') or
            (self.board[0][2]  == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X')):
            print("\nGame Over\nWinner: User")
            return True
        else: return not True
     
     def check_cpu(self):
        if ( # Check horizontally
            (self.board[0][0] == 'O' and self.board[0][1] == 'O' and self.board[0][2]) == 'O' or
            (self.board[1][0] == 'O' and self.board[1][1] == 'O' and self.board[1][2]) == 'O' or
            (self.board[2][0] == 'O' and self.board[2][1] == 'O' and self.board[2][2]) == 'O' or

            # Check vertically
            (self.board[0][0] == 'O' and self.board[1][0] == 'O' and self.board[2][0]) == 'O' or
            (self.board[0][1] == 'O' and self.board[1][1] == 'O' and self.board[2][1]) == 'O' or
            (self.board[0][2] == 'O' and self.board[1][2] == 'O' and self.board[2][2]) == 'O' or

            # Check diagonals
            (self.board[0][0]  == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O') or
            (self.board[0][2]  == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O')):
            print("\nGame Over\nWinner: CPU")
            return True
        else: return not True

            # Check if board is full (Tie)
     def check_tie(self):
        if (self.board[0][0] != ' ' and self.board[0][1] != ' ' and self.board[0][2] != ' ' and
            self.board[1][0] != ' ' and self.board[1][1] != ' ' and self.board[1][2] != ' ' and
            self.board[2][0] != ' ' and self.board[2][1]!= ' ' and self.board[2][2] != ' '):
           if self.check_user(): sys.exit()
           if self.check_cpu(): sys.exit()
           return True
        else: return not True

     def get_board(self):
        return self.board
     
     def display_board(self):
        print([' ','0', '1', '2'])
        current_board = self.get_board()
        i = 0
        for row in current_board:
            print(['{}'.format(i)] + row)
            i+=1
