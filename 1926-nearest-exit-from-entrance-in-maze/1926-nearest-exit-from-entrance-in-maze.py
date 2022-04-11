class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x, y = entrance
        m, n = len(maze), len(maze[0])
        reached = lambda p, q: (not p==x or not q==y) and (p==0 or q==0 or p==m-1 or q==n-1)
        q, ans = deque(), 0
        q.append((x, y, ans))
        directions = [1, 0, -1, 0, 1]
        while q:
            row, col, ans = q.popleft()
            if reached(row, col):
                return ans
            for i in range(4):
                r, c = row+directions[i], col+directions [i+1]
                if r<0 or c<0 or r==m or c==n or maze[r][c]=='+':
                    continue
                
                maze[r][c] = '+'
                q.append((r, c, ans+1))
        return -1