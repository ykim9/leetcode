class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            elif i == m - 1 or j == n - 1:
                return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)