class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 3:
            return [0, 1]
        d = {}
        for i, v in enumerate(nums):
            key = target - v
            if key in d:
                return [d[key], i]
            d[v] = i
        