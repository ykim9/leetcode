class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    mat[i][j] = -1 # 아직 처리되지 않은 값으로 표시
                else:
                    q.append((i, j)) # 값이 0인 좌표 저장
        
        # 0인 좌표에서 네 방향으로 확인
        DIR = [0, 1, 0, -1, 0]
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx, ny = x + DIR[d], y + DIR[d+1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n or mat[nx][ny] != -1:
                    continue
                mat[nx][ny] = mat[x][y] + 1
                q.append((nx, ny))
            
        
        return mat