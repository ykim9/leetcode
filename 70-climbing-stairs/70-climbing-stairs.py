class Solution:
    # 1번째는 1가지, 2번째는 2가지, 3번째는 3가지, 4번째는 5가지, 5번째는 8가지...
    # ways[n-1] + ways[n-2]가 정답
    # 방법 1
#     def climbStairs1(self, n: int) -> int:
#         if n <= 3:
#             return n
#         ways = [i+1 for i in range(n)]
        
#         for i in range(3, n):
#             ways[i] = ways[i - 1] + ways[i - 2]
            
#         return ways[-1]
    
    # 방법 2
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a