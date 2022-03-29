class Solution:
    def rob(self, nums: List[int]) -> int:
        max_rob = 0
        ans = [0] * len(nums)
        
        for i in range(len(nums)):
            if i < 2:
                max_rob = max(max_rob, nums[i])
                ans[i] = max_rob
                continue
            
            # 지금까지 강도 시나리오에서 제일 최고 이익이 되는 쪽과
            # 현재 위치 + 하나 떨어진 곳에서 얻은 최고 이익을 비교하여 높은 쪽 = 신규로 최고 이익 시나리오가 됨
            max_rob = max(max_rob, nums[i] + ans[i - 2])
            ans[i] = max_rob
            
        return max_rob