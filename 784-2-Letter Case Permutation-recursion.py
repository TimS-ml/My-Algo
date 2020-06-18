from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [S]
        for i, c in enumerate(S):
            if c.isalpha():
                res.extend([s[:i] + s[i].swapcase() + s[i + 1:] for s in res])
        return res


S = 'a1b2c3'
print(Solution().letterCasePermutation(S))
