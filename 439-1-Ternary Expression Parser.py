# https://leetcode-cn.com/problems/ternary-expression-parser/


class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        i = len(expression) - 1
        while i >= 0:
            if expression[i] not in ["?", ":"]:
                stack.append(expression[i])
            elif expression[i] == "?":
                i -= 1
                if expression[i] == "T":
                    top = stack.pop()
                    stack.pop()
                    stack.append(top)
                elif expression[i] == "F":
                    stack.pop()
            i -= 1
        return stack[0]

expression = "T?2:3"
print(Solution().parseTernary(expression))
