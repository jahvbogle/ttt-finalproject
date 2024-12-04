class TicTacToe:
     def __init__(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        
     #TODO Check for and prevent collisions
     def update_user(self, x, y):   
        self.board[x][y] = 'X'
        return self.board
     
     def update_cpu(self, x, y):
        self.board[x][y] = 'O'
        return self.board

     #TODO Check if goal state is reached
     def check_user(self):
        return not True
     
     def check_cpu(self):
        return not True
          
     def get_board(self):
        return self.board
      