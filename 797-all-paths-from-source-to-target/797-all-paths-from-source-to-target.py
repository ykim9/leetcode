class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(end, path):
            if end == len(graph) - 1:
                result.append(path)
                return
            for x in graph[end]:
                dfs(x, path+[x])
                
        result = []
        # from 0 to n - 1 node
        dfs(0, [0])
        return result