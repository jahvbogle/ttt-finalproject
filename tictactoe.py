class TicTacToe:
     def __init__(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        
     #TODO Prevent collisions
     def update_user(self, x, y):
        if not self.board[x][y] == ' ':
           print("\nInvalid move (User) (Position occupied: '{}' at row={} column={})"
                 .format(self.board[x][y], x, y))
        else:
           self.board[x][y] = 'X'
        return self.board
     
     def update_cpu(self, x, y):
        if not self.board[x][y] == ' ':
           print("\nInvalid move (CPU) (Position occupied: '{}' at row={} column={})"
                 .format(self.board[x][y], x, y))
        else:
           self.board[x][y] = '0'
        return self.board
     
     #TODO Check if goal state is reached
     def check_user(self):
        return not True
     
     def check_cpu(self):
        return not True
     
     def get_board(self):
        return self.board
     
     def display_board(self):
        print([' ','0', '1', '2'])
        current_board = self.get_board()
        i = 0
        for row in current_board:
            print(['{}'.format(i)] + row)
            i+=1
