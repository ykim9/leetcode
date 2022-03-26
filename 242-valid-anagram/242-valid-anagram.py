class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cntr = collections.defaultdict(int)
        for c in s:
            cntr[c] += 1
        
        for c in t:
            if not c in cntr or cntr[c] == 0:
                return False
            cntr[c] -= 1
        
        return all(i == 0 for i in cntr.values())