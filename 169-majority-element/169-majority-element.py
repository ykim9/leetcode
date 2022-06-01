class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        ans = nums[0]
        for n in nums:
            dic[n] += 1
            if n != ans and dic[n] > dic[ans]:
                ans = n
        
        return ans