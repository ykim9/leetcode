class Solution:
    # 이진수 n & 1의 결과: 마지막 수는 n의 마지막 수와 동일한 값
    # n & 1 후 n >> 1 오른쪽 시프트 연산하면 다음 숫자 n & 1 반복
    # 정답에 해당수를 더 해주고 왼쪽 시프트 비트 연산 후 다시 더하고 반복
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return n
        
        result = 0
        for i in range(32):
            result <<= 1
            result +=  n & 1
            n >>= 1
        return result