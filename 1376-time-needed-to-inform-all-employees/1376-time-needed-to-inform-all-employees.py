class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for i in range(n)]
        for i, m in enumerate(manager):
            if m >= 0: children[m].append(i)
        def dfs(i):
            mx = 0
            for j in children[i]:
                mx = max(mx, dfs(j))
            return mx + informTime[i]
        return dfs(headID)