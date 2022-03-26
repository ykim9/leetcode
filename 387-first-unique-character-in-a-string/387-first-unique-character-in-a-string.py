class Solution:
    def firstUniqChar(self, s: str) -> int:
        from string import ascii_lowercase
        letters = ascii_lowercase
        uniq = [s.index(l) for l in letters if s.count(l) == 1]
        return min(uniq) if uniq else -1
