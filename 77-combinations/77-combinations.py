class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(path, nums):
            if len(path) == k:
                result.append(path)
                return
            
            for i in range(len(nums)):
                dfs(path+[nums[i]], nums[i+1:])                  
        
        dfs([], list(range(1, n+1)))
        return result
    
#     def combine2(self, n: int, k: int) -> List[List[int]]:
#         result = []
#         def dfs(path, start, k):
#             if k == 0:
#                 return result.append(path[:])
                
#             for i in range(start, n + 1):
#                 path.append(i)              # 현재 값 추가
#                 dfs(path, i + 1, k - 1)     # 현재 값 다음의 값만 가능한 조합에 추가
#                 path.pop()                  
                
#         dfs([], 1, k)
#         return result
    
#     def combine3(self, n, k):
#         if k == 0:
#             return [[]]
#         return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
