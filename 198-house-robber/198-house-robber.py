class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        dp = nums[:]
        dp[1] = max(dp[0], dp[1])
        
        for i in range(2, len(nums)):
            # 지금까지 강도 시나리오에서 제일 최고 이익이 되는 쪽과
            # 현재 위치 + 하나 떨어진 곳에서 얻은 최고 이익을 비교하여 높은 쪽 = 신규로 최고 이익 시나리오가 됨
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            
        return dp[-1]