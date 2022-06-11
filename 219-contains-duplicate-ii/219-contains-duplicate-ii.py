class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0: return False
        
        dic = collections.Counter(nums[:k+1])
        if len(nums[:k+1]) != len(dic):
            return True
        
        for i in range(k+1, len(nums)):
            dic[nums[i-(k+1)]] -= 1
            if nums[i] in dic and dic[nums[i]] == 1:
                return True
            dic[nums[i]] = 1
        return False
