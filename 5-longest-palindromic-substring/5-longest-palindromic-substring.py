class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))] # 예 2:3번째 글자가 Palindrome이면True가됨
        for i in range(len(s)):
            dp[i][i] = True
        
        p_longest_start, p_longest_len = 0, 1
            
        for end in range(0, len(s)):
            for start in range(end-1,-1,-1):
                # i번째와 j번째 char가 같고, j와 i 인덱스 차이가 하나이면 palindrome임
                # i번째와 j번째 char가 같고, (i+1, j-1)번째 글자가 palindrome이면 True 
                #  예. 1:1과 4:4가 같은데 2:3번째 범위 글자가Palindrome이면 Palindrome (1+1, 4-3) 
                if s[start] == s[end]:
                    if start+1 == end or dp[start+1][end-1]:
                        dp[start][end] = True
                        palindrome_len = end - start + 1
                        if p_longest_len < palindrome_len:
                            p_longest_start = start
                            p_longest_len = palindrome_len
        return s[p_longest_start:p_longest_start+p_longest_len]