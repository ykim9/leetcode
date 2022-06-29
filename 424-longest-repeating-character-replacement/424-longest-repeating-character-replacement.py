class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = most_freq = left = 0
        cnt = collections.defaultdict(int)
        
        for right in range(len(s)):
            cnt[s[right]] += 1
            most_freq = max(most_freq, cnt[s[right]])
            if right - left + 1 - most_freq > k:
                cnt[s[left]] -= 1
                left += 1
            else:
                max_len = max(max_len, right - left + 1)
                        
        return max_len