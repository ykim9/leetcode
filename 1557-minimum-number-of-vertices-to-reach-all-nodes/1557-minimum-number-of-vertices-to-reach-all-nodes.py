class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for x, y in edges:
            indegree[y] += 1
        res = []
        print(indegree)
        for i, val in enumerate(indegree):
            if val == 0:
                res.append(i)
        
        return res