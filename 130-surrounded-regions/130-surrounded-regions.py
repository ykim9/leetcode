class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         def dfs(i, j):
#             board[i][j] = "-"
#             for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j - 1)):
#                 if 0 <= x < m  and 0 <= y < n and board[x][y] == "O":
#                     dfs(x, y)
        
#         m, n = len(board), len(board[0])
#         for i in range(m):
#             for j in range(n):
#                 if i not in (0, m -1) and j not in (0, n - 1):
#                     continue
#                 if board[i][j] == "O":
#                     dfs(i, j)
            
        
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == "O":
#                     board[i][j] = "X"
#                 elif board[i][j] == "-":
#                     board[i][j] = "O"
                    
    def solve(self, board: List[List[str]]) -> None:
        save = []
        m, n = len(board), len(board[0])
        for k in range(m+n):
            for ij in ((0, k), (m-1, k), (k, 0), (k, n - 1)):
                 save.append(ij)
            
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "-"
                save += [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            
        for row in board:
            for i, c in enumerate(row):
                row[i] = "OX"[c!="-"] 
                
                
        
        
            