class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        
        for i in range(200):
            if len(strs[0]) <= i:
                break
            pre = strs[0][i]
            for s in strs:
                if len(s) <= i or s[i] != pre:
                    return ans
            ans += pre
        return ans