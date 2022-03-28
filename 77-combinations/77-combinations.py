class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(path, start, k):
            if k == 0:
                return result.append(path[:])
                
            for i in range(start, n + 1):
                path.append(i)              # 현재 값 추가
                dfs(path, i + 1, k - 1)     # 현재 값 다음의 값만 가능한 조합에 추가
                path.pop()                  
                
        dfs([], 1, k)
        return result