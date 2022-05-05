class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        ans, cnt = 0, 0
        diff = nums[1] - nums[0]
        for i in range(1, len(nums)-1):
            cur_diff = nums[i+1] - nums[i]
            if diff == cur_diff:
                cnt += 1
            else:
                diff = cur_diff
                cnt = 0
                
            ans += cnt
        
        return ans
                
            
        