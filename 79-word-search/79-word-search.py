class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, visited, pos=0):
            if x < 0 or x >= m or y < 0 or y >= n or word[pos] != board[x][y] or (x, y) in visited:
                return False
            
            if pos == len(word) - 1:
                return True

            visited.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if dfs(x + dx, y + dy, visited, pos+1):
                    return True
            visited.remove((x, y))
            return False
        
        visited = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(i, j, visited):
                    return True
        return False
                    