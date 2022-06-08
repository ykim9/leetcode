class Solution:
    def isIsomorphic1(self, s: str, t: str) -> bool:
        return list(map(s.find, s)) == list(map(t.find, t))
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s, dic_t = {}, {}
        for sc, tc in zip(s, t):
            if sc not in dic_s and tc not in dic_t:
                dic_s[sc] = tc
                dic_t[tc] = sc
            elif (sc in dic_s and tc not in dic_t) or (sc not in dic_s and tc in dic_t):
                return False
            elif dic_s[sc] != tc or dic_t[tc] != sc:
                return False
        
        return True
    