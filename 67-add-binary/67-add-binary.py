class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        x, y = len(a) - 1, len(b) - 1
        carry = 0
        while x >= 0 or y >= 0:
            cur = carry
            if x >= 0:
                cur += int(a[x])
            if y >= 0:
                cur += int(b[y])
            
            ans += str(cur % 2)
            x, y = x - 1, y - 1
            carry = 1 if cur > 1 else 0
        
        
        if carry == 1:
            ans += str(carry)
        
        return ans[::-1]
            