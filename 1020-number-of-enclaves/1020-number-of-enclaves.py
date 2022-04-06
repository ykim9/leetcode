class Solution:
    # 외곽에 인접한 땅만 dfs로 방문해 모두 0으로 변경 후 육지의 수 세기
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = 0
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    dfs(x, y)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    dfs(i, j)
        return sum(sum(row) for row in grid)
    
#     def numEnclaves(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         def dfs(i, j):
#             if 0 > i or m <= i or 0 > j or n <= j:
#                 return (0, 0)
#             elif grid[i][j] == 0:
#                 return (1, 0)
            
#             isEnclave, cnt = 1, 1
#             grid[i][j] = 0
            
#             for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
#                 result = dfs(x, y)
#                 isEnclave *= result[0]
#                 cnt += result[1]
#             return (isEnclave, cnt)
        
#         ans = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     isEnclave, cnt = dfs(i, j)
#                     if isEnclave:
#                         ans += cnt
#         return ans