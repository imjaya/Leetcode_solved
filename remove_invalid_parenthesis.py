class Solution():

    def removeInvalidParentheses(self, s):
        if not s:
            return

        stack = []
        for i, token in enumerate(s):

            if token == ")" and stack and stack[-1][1] == "(":
                stack.pop()

            elif token in ('(',')'):
                stack.append((i,token))
            else:
                continue


        s = list(s)
        while stack:
            s.pop(stack.pop()[0])

        return ''.join(s)


obj = Solution()
assert obj.removeInvalidParentheses("ab(a(c)fg)9)))") == "ab(a(c)fg)9"
assert obj.removeInvalidParentheses(")a(b)c()(5") == "a(b)c()5"
assert obj.removeInvalidParentheses(")(") == ""
assert obj.removeInvalidParentheses("a(b))") == "a(b)"r