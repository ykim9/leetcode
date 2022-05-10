class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        
        for i in range(len(s)):
            for word in wordDict:
                if s[i-len(word)+1:i+1] == word and (i - len(word) == -1 or dp[i-len(word)]):
                    dp[i] = True
        
        return dp[-1]
                