class Solution:
    #DFS
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         def dfs(i):
#             for x in range(len(isConnected)):
#                 if isConnected[i][x] == 1 and x not in visited:
#                     visited.add(x)
#                     dfs(x)
                
#         ans = 0 
#         visited = set()
#         for i in range(len(isConnected)):
#             if i not in visited:
#                 dfs(i)
#                 ans += 1
#         return ans
    # iterative
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited, ans = set(), 0
        for i in range(len(isConnected)):
            if i not in visited:
                s = [i]
                while s:
                    num = s.pop()
                    if num not in visited:
                        visited.add(num)
                        s += [j for j, val in enumerate(isConnected[num]) if val == 1 and j not in visited]
                ans += 1
        return ans