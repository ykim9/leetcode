class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path):
            if not nums:
                res.append(path)
                return
            else:
                for i, v in enumerate(nums):
                    if i > 0 and v == nums[i - 1]:
                        continue
                    backtrack(nums[:i]+nums[i+1:], path+[v])
        
        res = []
        backtrack(sorted(nums), [])
        return res