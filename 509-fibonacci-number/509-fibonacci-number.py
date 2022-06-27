class Solution:
    # @cache
    # def fib1(self, n: int) -> int:
    #     if n <= 1: 
    #         return n
    #     return self.fib(n - 2) + self.fib(n - 1)
    
#     def fib2(self, n: int) -> int:
#         if n < 2:
#             return n
#         memo = [i for i in range(n + 1)]
#         for i in range(2, n + 1):
#             memo[i] = memo[i - 2] + memo[i - 1]
        
#         return memo[-1]
        
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a
    
    