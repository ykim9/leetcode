class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for num in digits:
            number = number * 10 + num
        
        number += 1
        
        ans = []
        while number > 0:
            ans.append(number % 10)
            number //= 10
        
        return ans[::-1]
            