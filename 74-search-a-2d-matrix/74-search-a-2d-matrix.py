class Solution:
    # row * col 값에서 binary search하는 방식
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
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
    
    # row와 col값을 각각 binary search하는 방식 
    def binary_search(self, row, target):
        start, end = 0, len(row) - 1
        while start <= end:
            mid = (start + end) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target and (mid < len(matrix) - 1 and target < matrix[mid + 1][0]) \
                or mid == len(matrix) - 1:
                    return self.binary_search(matrix[mid], target)
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False
    
    
    
