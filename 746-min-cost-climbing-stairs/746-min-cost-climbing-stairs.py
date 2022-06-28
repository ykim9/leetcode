class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = cost[:]
        for i in range(2, len(cost)):
            memo[i] = cost[i] + min(memo[i-2], memo[i-1])
        return min(memo[-1], memo[-2])