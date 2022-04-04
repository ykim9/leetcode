class Solution:
    def romanToInt(self, s: str) -> int:
        roman = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        ans = 0
        l, r = 0, 1
        while r < len(s):
            if roman[s[l]] < roman[s[r]]:
                ans += roman[s[r]] - roman[s[l]]
                l, r = r + 1, r + 2
            else:
                ans += roman[s[l]]
                l, r = r, r + 1
        if l == len(s) - 1:
            ans += roman[s[l]]
        return ans