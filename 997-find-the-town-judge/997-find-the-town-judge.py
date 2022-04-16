class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cnt = [0] * (n + 1)
        for a, b in trust:
            cnt[a] -= 1
            cnt[b] += 1
        
        for i in range(1, n + 1):
            if cnt[i] == n - 1:
                return i
        
        return -1