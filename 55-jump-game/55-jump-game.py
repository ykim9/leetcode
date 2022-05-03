class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        last = 0
        for i, n in enumerate(nums):
            if i == len(nums) -1:
                return True
            last -= 1
            if last <= 0 and n <= 0:
                return False
            if last < n:
                last = n
