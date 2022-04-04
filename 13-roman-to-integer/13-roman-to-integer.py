class Solution:
    def romanToInt(self, s: str) -> int:
        roman = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        ans = 0
        for i in range(1, len(s)):
            if roman[s[i - 1]] < roman[s[i]]:
                ans -= roman[s[i - 1]]
            else:
                ans += roman[s[i - 1]]
        
        return ans + roman[s[-1]]