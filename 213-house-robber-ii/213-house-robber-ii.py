class Solution:
    def rob(self, nums: List[int]) -> int:
        def do_rob(i, j):
            rob, not_rob = 0, 0
            for x in range(i, j):
                num = nums[x]
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)
        if len(nums) == 1:
            return nums[0]
        return max(do_rob(1, len(nums)), do_rob(0, len(nums)-1))