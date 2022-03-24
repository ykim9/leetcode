class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = {}
        left = longest = 0
        for right, c in enumerate(s):
            if c in counts and counts[c] >= left:
                left = counts[c] + 1
            longest = max(longest, right - left + 1)
            counts[c] = right
            
        return longest