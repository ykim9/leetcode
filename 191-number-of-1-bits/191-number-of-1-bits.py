class Solution:
    #방법 1: 비트연산 n&(n-1)은 가장 오른쪽 1값을 0으로 하는 것을 이용
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n:
            n &= n - 1
            answer += 1
        return answer
        
    
    #방법 2: binary를 string으로 바꿔서 1의 갯수 세기
    def hammingWeight2(self, n: int) -> int:
        return str(bin(n)).count("1")