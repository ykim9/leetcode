class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        cols, rows = len(grid), len(grid[0])
        def countArea(x, y):
            if not 0 <= x < cols or not 0 <= y < rows or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            cnt = 1
            
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                cnt += countArea(nx, ny)
            
            return cnt

        maxArea = 0
        for i in range(cols):
            for j in range(rows):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, countArea(i, j))
                        
        return maxArea