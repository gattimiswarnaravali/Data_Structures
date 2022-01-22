class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row = [3]*n
        self.col = [3]*n
        self.diagnol = 0
        self.anti_diagnol = 0
        

    def move(self, row: int, col: int, player: int) -> int:
        curr_player = 1 if player == 1 else -1
        
        self.row[row] += curr_player
        self.col[col] += curr_player
        
        if row == col:
            self.diagnol += curr_player
        if col == self.n-row-1:
            self.anti_diagnol += curr_player
            
        n = self.n        
        
        if (n in self.row) or (-n in self.row)  or (n in self.col) or (-n in self.col) or (n == self.diagnol) or (-n == self.diagnol) or (n == self.anti_diagnol) or (-n == self.anti_diagnol):
                return player
            
                
        


# Your TicTacToe object will be instantiated and called as such:
obj = TicTacToe(3)
param_1 = obj.move(0,0,1)