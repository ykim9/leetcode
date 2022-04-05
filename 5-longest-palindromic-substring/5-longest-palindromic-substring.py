class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        dp = [[False] * len(s) for _ in range(len(s))] # 예 2:3번째 글자가 Palindrome이면True가됨
        for i in range(len(s)):
            dp[i][i] = True
            res = s[i]
            
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1, len(s)):
                # i번째와 j번째 char가 같고, j와 i 인덱스 차이가 하나이면 palindrome임
                # i번째와 j번째 char가 같고, (i+1, j-1)번째 글자가 palindrome이면 True 
                #  예. 1:1과 4:4가 같은데 2:3번째 범위 글자가Palindrome이면 Palindrome (1+1, 4-3) 
                if s[i] == s[j]:
                    if i+1 == j or dp[i+1][j-1]:
                        dp[i][j] = True
                        if len(res) < len(s[i:j+1]):
                            res = s[i:j+1]
        return res