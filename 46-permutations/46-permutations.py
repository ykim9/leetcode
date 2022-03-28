class Solution:
    # solution 1
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(track, nums):
            # 모든 값을 선택하여 조합하였으면 결과값에 추가하고 재귀 종료
            if not len(nums):
                return result.append(track)
                
            #자기 자신을 제외한 값 중에 선택하여 진로에 덧붙이기
            for i in range(len(nums)):
                dfs(track+[nums[i]], nums[:i]+nums[i+1:])
        
        dfs([], nums)
        return result
    
    # solution2
    def permute2(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(start, end):
            if start == end:
                return result.append(nums[:])
                
            for i in range(start, end):
                nums[start], nums[i] =  nums[i], nums[start] #자기 자신을 제외한 값 중에 탐색하도록 위치 변경
                dfs(start+1, end)
                nums[i], nums[start] = nums[start], nums[i]  #다음 번호 탐색을 위하여 복구
        
        dfs(0, len(nums))
        return result