class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sl, pl = len(s), len(p)
        if sl < pl:
            return []
        
        res = []
        pc = collections.Counter(p)
        sc = None
        for i in range(sl - pl + 1):
            if i == 0:
                sc = collections.Counter(s[:pl])
            else:
                sc[s[i - 1]] -= 1
                sc[s[i + pl - 1]] += 1
            if pc == sc:
                res.append(i)
        
        return res
            