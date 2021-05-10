class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        result = ''
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == "[":
                stack.append(result)
                stack.append(num)
                result = ''
                num = 0
            elif c.isalpha():
                result += c
            elif c == ']':
                pre_num = stack.pop()
                pre_string = stack.pop()
                result = pre_string + pre_num * result
        return result
                
        