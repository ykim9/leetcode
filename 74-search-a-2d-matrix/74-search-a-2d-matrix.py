class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])
        start, end = 0, len(matrix) * len(matrix[0]) - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid // col][mid % col] == target:
                return True
            elif matrix[mid // col][mid % col] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
