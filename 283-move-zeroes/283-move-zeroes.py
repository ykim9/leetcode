class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        for num in nums:
            if num != 0:
                nums[x] = num
                x += 1
            
        for i in range(x, len(nums)):
            nums[i] = 0