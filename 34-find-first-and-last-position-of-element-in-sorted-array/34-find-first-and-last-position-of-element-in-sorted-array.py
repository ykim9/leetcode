class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        def find_start_point(mid):
            l = r = mid
            while 0 <= l and nums[l] == target:
                l -= 1
            while r < len(nums) and nums[r] == target:
                r += 1
            return [l + 1, r - 1]
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid =  (l + r )// 2 
            print(mid, l, r)
            if nums[mid] == target:               
                #find starting point and ending poitn
                return find_start_point(mid)
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return [-1, -1]