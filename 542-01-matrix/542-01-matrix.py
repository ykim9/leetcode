class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # initialization
        m, n = len(mat), len(mat[0])
        visited = set()
        queue = collections.deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j))
        dirs = [0, 1, 0, -1, 0]
        
        #BFS
        while queue:
            i, j = queue.popleft()
            for x in range(1, len(dirs)):
                ni, nj = i + dirs[x-1], j + dirs[x]
                if 0 <= ni < m and 0 <= nj < n:
                    if (ni, nj) not in visited and mat[ni][nj] == 1:
                        visited.add((ni, nj))
                        queue.append((ni, nj))
                        mat[ni][nj] = mat[i][j] + 1
                        
                        
        return mat