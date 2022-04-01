class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result
        
        rowStart, rowEnd = 0, len(matrix) - 1
        colStart, colEnd = 0, len(matrix[0]) - 1
        while rowStart <= rowEnd and colStart <= colEnd:
            for x in range(colStart, colEnd + 1):
                result.append(matrix[rowStart][x])
            rowStart += 1
            if rowStart > rowEnd: break

            for x in range(rowStart, rowEnd + 1):
                result.append(matrix[x][colEnd])
            colEnd -= 1
            if colStart > colEnd: break

            for x in range(colEnd, colStart - 1, -1):
                result.append(matrix[rowEnd][x])
            rowEnd -= 1
            if rowStart > rowEnd: break
                
            for x in range(rowEnd, rowStart - 1, -1):
                result.append(matrix[x][colStart])
            colStart += 1
                
        return result