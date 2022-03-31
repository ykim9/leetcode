class Solution:
    # xor: 같은 수를 짝수 번 xor연산하는 경우의 결과는 0
    # 0에 숫자 n을 xor연산 하면 결과 값은 n 자신이 나옴
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans