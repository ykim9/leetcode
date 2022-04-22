class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, track):
            if index == len(digits):
                return ans.append(track)
            
            for c in pn[digits[index]]:
                dfs(index + 1, track + c) 
                
        if digits == "": return []
        
        ans = []
        pn = {"2": "abc", "3": "def", "4": "ghi", "5":"jkl", "6": "mno", "7": "pqrs", "8":"tuv", "9": "wxyz"}
        
        dfs(0, "")
        return ans