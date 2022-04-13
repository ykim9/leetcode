class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def dfs(i):
            if seen[i]:
                return
            seen[i] = True
            for x in pc[i]:
                dfs(x)
                
        if len(connections) < n - 1:
            return -1
        
        seen = [False] * n
        pc = [set() for _ in range(n)]
        for i, j in connections:
            pc[i].add(j)
            pc[j].add(i)

        ans = 0
        for i in range(n):
            if not seen[i]:
                dfs(i)
                ans += 1
        return ans - 1
        