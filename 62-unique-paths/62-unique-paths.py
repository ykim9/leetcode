class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [1] * n
#         for _ in range(1, m):
#             for j in range(1, n):
#                 dp[j] += dp[j-1]
#         return dp[n-1]
    
    def uniquePaths(self, m: int, n: int) -> int:
        # 아래로 가는 m-1, 오른쪽으로 가는 n-1 가지 경우 m+n-2개 이동 방식에서 
        return factorial(m+n-2) // (factorial(m - 1) * factorial(n - 1))