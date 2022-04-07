class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        if len(q) == m * n:
            return -1
        
        level = -1
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j -1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = 1
                        q.append((x, y))
            level += 1
        return level 