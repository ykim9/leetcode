class Solution:
    def jump(self, nums: List[int]) -> int:

        ans, max_jump, last_jump  = 0, 0, 0
        for i in range(len(nums) - 1):
            max_jump = max(max_jump, i+nums[i])
            
            if last_jump == i:
                last_jump = max_jump
                ans += 1
                
                
        return ans
            