class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(x, y):
            if x in (-1, m) or y in (-1, n) or grid2[x][y] == 0:
                return 1
            
            isSub = True
            if grid1[x][y] == 0 and grid2[x][y] == 1:
                isSub = False
                #keep sink the island
                
            grid2[x][y] = 0
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y -1)):
                isSub *= dfs(i, j)
            return isSub
        
        m, n = len(grid1), len(grid1[0])
        ans = 0
        for x in range(m):
            for y in range(n):
                if grid1[x][y] == 1 and grid2[x][y] == 1:
                    if dfs(x, y):
                        ans += 1
        return ans
                    