from dataclasses import dataclass

@dataclass
class NumberQueens:
    n: int
    chess_table: list[list[int]] | None = None
    
    def __post_init__(self):
        if self.chess_table is None:
            self.chess_table = [[0 for i in range(self.n)] for j in range(self.n)]
    
    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print('Q', end=' ')
                else:
                    print('_', end=' ')
            print()
    
    def isSafe(self, row: int, col: int):
        # Horizontal check
        for i in range(self.n):
            if self.chess_table[row][i] == 1:
                return False
        
        # Vertical check
        for i in range(self.n):
            if self.chess_table[i][col] == 1:
                return False
        
        # Diagonal check left up-bottom
        j = col
        for i in range(row, -1, -1):
            if self.chess_table[i][j] == 1:
                return False
            j -= 1

        # Diagonal check right bottom-up
        j = col
        for i in range(self.n):
            if j >= self.n:
                break
            if self.chess_table[i][j] == 1:
                return False
            j += 1    
        
        return True
    
    def solve(self, col: int = 0):
        if col == self.n:
            return True
        for i in range(self.n):
            if self.isSafe(row=i, col=col):
                self.chess_table[i][col] = 1
                if self.solve(col + 1):
                    return True
                self.chess_table[i][col] = 0
        return False
