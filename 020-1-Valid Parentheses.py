# https://leetcode-cn.com/problems/valid-parentheses/
# 空字符串可被认为是有效字符串
# 从右往左，如果遇到一个新括号，就需要先结束新括号


class Solution:
    def isValid(self, s) -> bool:
        if len(s) == 0:
            return True

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        # print(mapping[")"])

        for char in s:
            if char in mapping:  # 找右括号，无论是()[]，还是({})，遇到第一个右括号的时候边上必有左括号
                top_element = stack.pop() if stack else '#'  # 对应append的左括号
                print(stack)
                # print("top", top_element)
                # print("mapping", mapping[char])
                if mapping[char] != top_element:  # 对应正确的左括号，mapping[")"] = "("
                    return False
            else:
                stack.append(char)  # 添加非右括号
        # The stack won't be empty for cases like ((() !!! 这算是另一种特殊情况
        return not stack


IN = [("{[]}"), ("([)]"), ("(((())))")]
useSet = 0
print(IN[useSet])
print(Solution().isValid(IN[useSet]))

