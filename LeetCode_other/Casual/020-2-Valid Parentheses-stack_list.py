# https://leetcode-cn.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s) -> bool:
        if len(s) == 0:
            return True

        stack = []
        mapping = ["()", "[]", "{}"]

        for i in range(0, len(s)):
            stack.append(s[i])
            # 比如i = 2的时候，stack = "{[]"
            # 直觉上不太严谨，实际上是可行的……
            if len(stack) >= 2 and stack[-2] + stack[-1] in mapping:
                stack.pop()
                stack.pop()
        return len(stack) == 0


IN = [("{[]}"), ("([)]"), ("(((())))")]
useSet = 0
print(IN[useSet])
print(Solution().isValid(IN[useSet]))
