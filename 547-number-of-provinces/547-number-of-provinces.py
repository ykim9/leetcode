class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            for x in range(len(isConnected)):
                if isConnected[i][x] == 1 and x not in visited:
                    visited.add(x)
                    dfs(x)
                
        ans = 0 
        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans