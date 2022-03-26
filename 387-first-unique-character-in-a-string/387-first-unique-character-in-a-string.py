class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = [1] * len(s)
        cnt = {}
        for i, c in enumerate(s):
            if c in cnt:
                unique[i] = 0
                unique[cnt[c]] = 0
            else:
                cnt[c] = i
                
        try:
            return unique.index(1)
        except:
            return -1
        
