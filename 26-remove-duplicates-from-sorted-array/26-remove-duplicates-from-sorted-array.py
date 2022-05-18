class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            if x == 0 or nums[x-1] != num:
                nums[x] = num
                x += 1
        return x