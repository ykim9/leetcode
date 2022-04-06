class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if 0 > i or m <= i or 0 > j or n <= j:
                return (0, 0)
            elif grid[i][j] == 0:
                return (1, 0)
            
            isEnclave, cnt = 1, 1
            grid[i][j] = 0
            
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            
                result = dfs(x, y)
                isEnclave *= result[0]
                cnt += result[1]
            return (isEnclave, cnt)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    isEnclave, cnt = dfs(i, j)
                    if isEnclave:
                        ans += cnt
        return ans