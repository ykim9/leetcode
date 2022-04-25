class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        s = left = 0
        for right in range(len(nums)):
            s += nums[right]
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return ans if ans <= len(nums) else 0