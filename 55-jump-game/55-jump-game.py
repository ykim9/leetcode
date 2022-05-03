class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        for i, n in enumerate(nums):
            if jump < i:
                return False
            jump = max(jump, n + i)
        return True