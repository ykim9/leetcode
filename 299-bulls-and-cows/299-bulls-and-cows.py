class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = cow = 0
        s_cnt = collections.defaultdict(int)
        g_cnt = collections.defaultdict(int)
        for i, c in enumerate(secret):
            if c == guess[i]:
                bull += 1
            
            s_cnt[c] += 1
            g_cnt[guess[i]] += 1
            
        for c in s_cnt:
            if c in g_cnt:
                cow += min(s_cnt[c], g_cnt[c])
                
        cow = cow - bull if cow - bull > 0 else 0
                
        return f'{bull}A{cow}B'
                