class Solution:
    grid: List[List[str]]
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                for x, y in ((i-1, j), (i+1, j), (i, j -1), (i, j + 1)):
                    dfs(x, y)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        
        return ans