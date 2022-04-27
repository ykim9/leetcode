class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path):
            result.append(path[:])
            for i, n in enumerate(nums):
                if 0 < i and nums[i] == nums[i -1]:
                    continue
                path.append(n)
                dfs(nums[i+1:], path)
                path.pop()
                
        result = []
        dfs(sorted(nums), [])
        return result