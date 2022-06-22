class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = collections.Counter(s)
        ans = 0
        addMidChar = 0
        for c in cnt:
            if cnt[c] % 2 == 0:
                ans += cnt[c]
            else:
                addMidChar = 1
                if cnt[c] > 2:
                    ans += cnt[c] - 1
                    
        return ans + addMidChar