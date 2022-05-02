class Solution:
    def rob(self, nums: List[int]) -> int:
        def do_rob(i, j):
            last, now = 0, 0
            for x in range(i, j):
                num = nums[x]
                last, now = now, max(last + num, now)
            return now
        if len(nums) == 1:
            return nums[0]
        return max(do_rob(1, len(nums)), do_rob(0, len(nums)-1))