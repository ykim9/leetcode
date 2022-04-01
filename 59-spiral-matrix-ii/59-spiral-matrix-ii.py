class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        result = [[0] * n for _ in range(n)]
        rowStart, rowEnd = 0, n - 1
        colStart, colEnd = 0, n - 1
        num = 1
        while rowStart <= rowEnd and colStart <= colEnd:
            for x in range(colStart, colEnd + 1):
                result[rowStart][x] = num
                num += 1
            rowStart += 1
            
            for x in range(rowStart, rowEnd + 1):
                result[x][colEnd] = num
                num += 1
            colEnd -= 1
            
            for x in range(colEnd, colStart - 1, -1):
                result[rowEnd][x] = num
                num += 1
            rowEnd -= 1
            
            for x in range(rowEnd, rowStart - 1, -1):
                result[x][colStart] = num
                num += 1
            colStart += 1
            
        return result
        