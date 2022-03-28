class Solution:
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