class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        if len(set(words)) != len(set(pattern)):
            return False
        
        dic = {}
        for i, c in enumerate(pattern):
            if c not in dic:
                dic[c] = words[i]
            elif dic[c] != words[i]:
                return False
        return True
            
            