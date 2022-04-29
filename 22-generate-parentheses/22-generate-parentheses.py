class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(n):
            cnt = 0
            for c in n:
                if c == "(": cnt +=1
                else:
                    if cnt == 0: return 0
                    cnt -= 1
            return cnt == 0

        def generate(path=''):
            if len(path) == n * 2:
                if isValid(path):
                    res.append(path)
            else:
                generate(path+"(")
                generate(path+")")
                
        res = []
        generate()
        return res