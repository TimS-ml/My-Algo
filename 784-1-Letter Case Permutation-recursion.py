# [""]
# ["a", "A"]
# ["ab", "aB", "Ab", "AB"]  # copy then append
from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return [""]

        index = -1
        for i in range(len(S)):
            if S[i].isalpha():
                index = i  # the i-th number
                break
        if index == -1:
            return [S]
        else:
            tmp = self.letterCasePermutation(S[index + 1:])
            ans = []
            for s in tmp:  # append
                ans.append(S[:index] + S[index].lower() + s)
                ans.append(S[:index] + S[index].upper() + s)
            return ans


S = 'a1b2c3'
print(Solution().letterCasePermutation(S))