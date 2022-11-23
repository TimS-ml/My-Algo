'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)
'''


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
                continue
            else:
                stack.append(c)

        return ''.join(stack)


s = 'abbaca'
print(Solution().removeDuplicates(s))
print(Solution().removeDuplicates_2(s))
