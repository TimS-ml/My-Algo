'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)



left==0相当于左右括号的平衡
'''


class Solution:
    def generateParenthesis(self, n: int):
        def backtrack(subStr, left, right):
            # or use if right == n
            if len(subStr) == 2 * n:
                ans.append(subStr)
                return
            # if left < n and if right < left will keep balance
            if left < n:
                # print('before 1:', subStr)
                backtrack(subStr + '(', left + 1, right)
                # print('after 1:', subStr)
            if right < left:
                # print('before 2:', subStr)
                backtrack(subStr + ')', left, right + 1)
                # print('after 2:', subStr)

        ans = []
        backtrack('', 0, 0)
        return ans

    # same... but we need to check if left is 0
    # other wise will include '()()(('
    def generateParenthesis_2(self, n: int):
        def backtrack(left, subPath):
            if len(subPath) == 2 * n:
                if left == 0:
                    ans.append(''.join(subPath))
                # ans.append(''.join(subPath))
                return

            if left < n:
                subPath.append('(')
                backtrack(left + 1, subPath)
                subPath.pop()  # len(subPath) == 2*n and left != 0
            if left > 0:
                subPath.append(')')
                backtrack(left - 1, subPath)
                subPath.pop()

        ans = []
        backtrack(0, [])
        return ans


print(Solution().generateParenthesis(3))
# print(Solution().generateParenthesis_2(3))
