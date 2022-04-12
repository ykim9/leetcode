class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        
        n = len(graph)
        stack = [(0, [0])]
        res = []
        while stack:
            node, path = stack.pop(0)
            if node == n - 1:
                res.append(path)
            
            for x in graph[node]:
                stack.append((x, path + [x]))
        
        return res
        
            
    
# dfs
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         def dfs(end, path):
#             if end == len(graph) - 1:
#                 result.append(path)
#                 return
#             for x in graph[end]:
#                 dfs(x, path+[x])
                
#         result = []
#         # from 0 to n - 1 node
#         dfs(0, [0])
#         return result