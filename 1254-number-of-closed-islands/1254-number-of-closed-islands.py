class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # 닫힌 섬인지 확인하기
        def isClosedIsland(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            
            if grid[i][j] == 1:
                return 1
            
            grid[i][j] = 1
            DIR = [0, 1, 0, -1, 0]
            isClosed = 1
            for x in range(1, len(DIR)):
                ni, nj = i + DIR[x-1], j + DIR[x]
                isClosed *= isClosedIsland(ni, nj)
            return isClosed
                    
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:                  #섬이고 닫혀 있으면 count 추가하기
                    count += isClosedIsland(i, j)
        return count