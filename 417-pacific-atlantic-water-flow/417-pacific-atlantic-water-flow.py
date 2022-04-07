class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r, c = len(heights), len(heights[0])
        visited_p = set()
        visited_a = set()
        def dfs(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            
            for x, y in [(i + 1, j),(i - 1, j),(i, j + 1),(i, j - 1)]:
                if 0 <= x < r and 0 <= y < c:
                    if heights[i][j] <= heights[x][y]:
                        dfs(x, y, visited)
                        
        
        for row in range(r):
            dfs(row, 0, visited_p)
            dfs(row, c-1, visited_a)
            
        for col in range(c):
            dfs(0, col, visited_p)
            dfs(r-1, col, visited_a)
                
        return list(visited_p & visited_a)