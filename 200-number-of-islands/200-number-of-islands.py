class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "0"
                list(map(dfs, (i-1, i+1, i, i), (j, j, j-1, j+1)))
                return 1
            return 0
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += dfs(i, j)
        return ans