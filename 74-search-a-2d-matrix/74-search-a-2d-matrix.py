class Solution:
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
        r1, r2 = 0, len(matrix) - 1
        while r1 <= r2:
            mid = (r1 + r2) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target and (mid < len(matrix) - 1 and target < matrix[mid + 1][0]) \
                or mid == len(matrix) - 1:
                    return self.binary_search(matrix[mid], target)
            elif matrix[mid][0] > target:
                r2 = mid - 1
            else:
                r1 = mid + 1
        return False