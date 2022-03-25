class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check for row
        for row in board:
            if any(row.count(i) > 1 for i in row if i != "."):
                return False
        
        # check for column
        for col in zip(*board):
            if any(col.count(i) > 1 for i in col if i != "."):
                return False
        
        # check for 3*3 sub-boxes
        for k in range(0, 9, 3):
            r = board[:k+3]
            subBox = [[], [], []]
            for i in range(k, k+3):
                for j in range(3):
                    subBox[j] += r[i][j*3:j*3+3]
            
            for b in subBox:
                if any(b.count(i) > 1 for i in b if i != "."):
                    return False
            
        return True
        