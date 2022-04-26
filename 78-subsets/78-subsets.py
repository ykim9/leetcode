class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path):
            result.append(path)
            for i, n in enumerate(nums):
                dfs(nums[i+1:], path+[n])
                
        result = []
        dfs(nums, [])
        return result