class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        orange = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    orange.append((i, j, 0))
            
        DIR = [0, -1, 0, 1, 0]
        minute = 0
        while orange:
            x, y, _min = orange.pop(0)
            minute = _min
            for i in range(4):
                nx, ny = x + DIR[i], y + DIR[i+1]
                if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != 1:
                    continue
                grid[nx][ny] = 2
                orange.append((nx, ny, _min + 1))
        
        
        return -1 if any(1 for row in grid for orange in row if orange == 1) else minute