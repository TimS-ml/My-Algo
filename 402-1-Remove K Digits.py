# https://leetcode-cn.com/problems/remove-k-digits/


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k>0 and stack and stack[-1]>c:
                stack.pop()
                print("pop", stack)
                k -= 1
            stack.append(c)
            print("append", stack)
        if k>0:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"


num1, k1 = "1432219", 3
num2, k2 = "10200", 1
num3, k3 = "10", 2
print(Solution().removeKdigits(num1, k1))
