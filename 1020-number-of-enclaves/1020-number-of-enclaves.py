class Solution:
    def dfs(self, grid, visited, i, j):
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
            return -1
        if grid[i][j] == 0:
            return 0
        if (i, j) in visited:
            return 0
        visited.add((i, j))
        result = [self.dfs(grid, visited, x, y) for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]]
        for r in result:
            if r == -1:
                return r
        return 1 + sum(result)
        
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = set()
        result = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    temp = self.dfs(grid, visited, i, j)
                    if temp > 0:
                        result += temp
        return result
    
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