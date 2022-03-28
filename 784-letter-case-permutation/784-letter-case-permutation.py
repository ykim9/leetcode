class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = ['']
        for c in s:
            # 글자가 알파벳인 경우
            if c.isalpha():
                # result list에 있는 항목들에 각각 대문자와 더한 값과 소문자를 더한 값을 하나씩 추가한다.
                # result 크기는 기존의 두배가 된다
                result = [r + alpha for r in result for alpha in (c.lower(), c.upper())]
            else:
                result = [r + c for r in result] # result list안의 항목들에 숫자를 덧붙인다.
        return result