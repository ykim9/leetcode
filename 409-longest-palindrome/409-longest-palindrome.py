class Solution:
    # def longestPalindrome(self, s: str) -> int:
    #     ans = 0
    #     for n in collections.Counter(s).values():
    #         ans += (n // 2) * 2
    #         if ans % 2 == 0 and n % 2 == 1:
    #             ans += 1
    #     return ans
    
    # count odds
    def longestPalindrome(self, s: str) -> int:
        odds = sum([n % 2 == 1 for n in collections.Counter(s).values()])
        return len(s) - odds + bool(odds)
    