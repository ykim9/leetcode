class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ''
        cur_s = ''
        cur_num = 0
        for c in s:
            if c.isdigit():
                cur_num = (cur_num * 10) + int(c)
            elif c.isalpha():
                cur_s += c
            elif c == '[':
                stack.append(cur_s)
                stack.append(cur_num)
                cur_num = 0
                cur_s = ''
            elif c == ']':
                repeat = stack.pop()
                cur_s = stack.pop() + cur_s * repeat
        
        return cur_s