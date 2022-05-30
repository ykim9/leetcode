class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        ans = ''
        while n > 0:
            n, mod = divmod(n - 1, 26)
            ans += chr(mod + ord('A'))
            
        return ans[::-1]