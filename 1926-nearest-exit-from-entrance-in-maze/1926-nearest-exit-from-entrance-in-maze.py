class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x, y = entrance
        m, n = len(maze), len(maze[0])
        q = deque([(x, y, 0)])
        dirs = [1, 0, -1, 0, 1]
        maze[x][y] = '+'
        while q:
            row, col, ans = q.popleft()
            for i in range(4):
                r, c = row+dirs[i], col+dirs[i+1]
                if r < 0 or c < 0 or r == m or c == n or maze[r][c] == '+':
                    continue
                if r == 0 or c == 0 or r == m - 1 or c == n - 1:
                    return ans + 1
                maze[r][c] = '+'
                q.append((r, c, ans+1))
        return -1