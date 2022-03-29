class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(", "]":"[", "}":"{"}
        for p in s:
            if p in dic:                               # 닫는 괄호일 경우
                # stack이 비었거나 stack의 pop값과 dict[p]가 일치하지 않으면 False
                if not stack or dic[p] != stack.pop():   
                    return False
            else:                                       # 여는 괄호일 경우, 혹은 그외 닫는 괄호가 아닌 경우
                stack.append(p)                         # stack에 push
        
        return len(stack) == 0                          # stack에 모든 값이 pop되지 않은 경우는 False
        