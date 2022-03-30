class Solution:
    # 기본 아이디어:
    # 아랫줄에서부터 윗줄로 연산
    # 더했을 때 가장 작은 값인 것 계산하여 최소값 계산
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(row + 1):
                triangle[row][i] += min(triangle[row+1][i], triangle[row+1][i+1])
        return triangle[0][0]
    
    # input값 변경 없이 연산하기
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        cur_row, next_row = [0] * n, triangle[n-1]
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(row + 1):
                cur_row[i] = triangle[row][i] + min(next_row[i], next_row[i+1])
            cur_row, next_row = next_row, cur_row
        return next_row[0]