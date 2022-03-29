class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in ("(", "[", "{"):         # 여는 괄호는 stack에 push
                stack.append(p)
            elif p in (")", "]", "}"):
                if not stack:
                    return False
                last = stack.pop()           # stack에서 pop한 원소와 닫는 괄호 모양이 일치하지 않으면 False 
                if (p == ")" and last != "(") or (p == "]" and last != "[") or (p == "}" and last != "{"):
                    return False
            else:
                continue
        return False if len(stack) else True
                    