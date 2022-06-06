class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_squares(num):
            res = 0
            while num != 0:
                num, mod = divmod(num, 10)
                res += (mod % 10) ** 2
            return res
        
        s = set()
        while n != 1:
            n = sum_squares(n)
            if n in s:
                return False
            s.add(n)
        return True
            