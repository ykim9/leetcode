class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(r, c, path=[]):
            if r < 0 or r >= m or c < 0 or c >= n or land[r][c] == 0:
                return (0, 0)
            
            land[r][c] = 0
            
            nr1, nc1 = dfs(r + 1, c)
            nr2, nc2 = dfs(r, c + 1)
            
            nr = max(nr1, nr2, r)
            nc = max(nc1, nc2, c)
            return nr, nc
                
        ans = []
        m, n = len(land), len(land[0])
        for r in range(m):
            for c in range(n):
                if land[r][c] == 1:
                    i, j = dfs(r, c)
                    ans.append([r, c, i, j])
        return ans