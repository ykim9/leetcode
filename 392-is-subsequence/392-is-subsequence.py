class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:   return True
        if not t:   return False
        
        x = 0
        for c in t:
            if c == s[x]:
                x += 1
                if x == len(s):
                    return True
        
        return x == len(s)