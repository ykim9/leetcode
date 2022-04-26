class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i, j):
            board[i][j] = "-"
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j - 1)):
                if 0 <= x < m  and 0 <= y < n and board[x][y] == "O":
                    dfs(x, y)
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if i not in (0, m -1) and j not in (0, n - 1):
                    continue
                if board[i][j] == "O":
                    print("dfs")
                    dfs(i, j)
            
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "-":
                    board[i][j] = "O"