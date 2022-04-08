class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        visit = set()
        queue = collections.deque([(0, 0, 1)]) # row. col. dist
        visit.add((0, 0))
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while queue:
            i, j, dist = queue.popleft()
            if i == n - 1 and j == n - 1:
                return dist
            for x, y in dirs:
                ni, ny = i+x, j+y
                if 0 > ni or ni >= n or 0 > ny or ny >= n:
                    continue
                if (ni, ny) not in visit and grid[ni][ny] == 0:
                    queue.append((ni, ny, dist + 1))
                    visit.add((ni, ny))
                    
        return -1                    