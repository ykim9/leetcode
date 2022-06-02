class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i, c in enumerate(columnTitle[::-1]):
            ans += (26 ** i) * (ord(c) - ord('A') + 1)
        return ans