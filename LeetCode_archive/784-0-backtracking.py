'''
# Code Explain:
- Time complexity: O(N * 2^N)
- Space complexity: O(N * 2^N)

'''

from typing import List


class Solution(object):

    def letterCasePermutation(self, S: str) -> List[str]:
        def backtrack(subset, start):
            # at leaf
            if len(subset) == len(S):
                ans.append(subset)
            else:
                if S[start].isalpha():
                    backtrack(subset + S[start].swapcase(), start + 1)
                backtrack(subset + S[start], start + 1)

        ans = []
        backtrack('', 0)
        return ans

    def letterCasePermutation_2(self, S: str) -> List[str]:
        ans = [[]]

        for char in S:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n + i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)

        return map("".join, ans)

    def letterCasePermutation_3(self, S: str) -> List[str]:
        ans = [S]
        for i, c in enumerate(S):
            if c.isalpha():
                ans.extend([s[:i] + s[i].swapcase() + s[i + 1:] for s in ans])
        return ans


S = 'a1b2c3'
print(Solution().letterCasePermutation(S))
