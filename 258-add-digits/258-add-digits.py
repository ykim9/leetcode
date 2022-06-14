class Solution:
    # def addDigits(self, num: int) -> int:
    #     while num >= 10:
    #         num = sum([int(n) for n in str(num)])
    #     return num
    
    def addDigits(self, num: int) -> int:
        if num == 0:
            return num
        return 9 if num % 9 == 0 else num % 9 