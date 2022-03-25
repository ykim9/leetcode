class Solution:
    def isValidArray(self, array):
        array = [i for i in array if i != "."]
        return len(set(array)) == len(array)
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for row
        for row in board:
            if not self.isValidArray(row):
                return False
        
        # check for column
        for col in zip(*board):
            if not self.isValidArray(col):
                return False
        
        # check for 3*3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subBox = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]        
                if not self.isValidArray(subBox):
                    return False
        
        return True
        