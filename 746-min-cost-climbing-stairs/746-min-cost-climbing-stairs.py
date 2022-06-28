class Solution:
#     def minCostClimbingStairs1(self, cost: List[int]) -> int:
#         def dp(n):
#             if n < 2:
#                 return cost[n]
#             return cost[n] + min(dp(n-1), dp(n-2))
#         length = len(cost)
#         return min(dp(length-1), dp(length-2))
    
#     def minCostClimbingStairs2(self, cost: List[int]) -> int:
#         memo = cost[:]
#         for i in range(2, len(cost)):
#             memo[i] = cost[i] + min(memo[i-2], memo[i-1])
#         return min(memo[-1], memo[-2])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        
        fst, sec = cost[0], cost[1]
        for i in range(2, len(cost)):
            cur = cost[i] + min(fst, sec)
            fst, sec = sec, cur
        
        return min(fst, sec)