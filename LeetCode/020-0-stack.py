'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)
'''


class Solution:
    def isValid(self, s) -> bool:
        if len(s) == 0:
            return True

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:  # if right parenthesis
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:  # Example: mapping[")"] = "("
                    return False
            else:
                stack.append(char)  # right parenthesis
        # The stack won't be empty for cases like ((() !!!
        return not stack

    def isValid_2(self, s) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            elif not stack or char != stack.pop():
                return False
        return not stack


# s = "{[]}"
# s = "([)]"
s = "(((())))"
print(Solution().isValid(s))
