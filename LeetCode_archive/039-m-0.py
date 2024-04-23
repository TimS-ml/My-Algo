'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(temp, idx):
            # forget about terminate '>'
            if sum(temp) == target:
                ans.append(temp[:])
            if sum(temp) > target:
                return

            for i in range(idx, len(candidates)):
                temp.append(candidates[i])
                helper(temp, i)
                temp.pop()
        
        ans = []
        helper([], 0)
        return ans


c = [2,3,6,7]
t = 7
print(Solution().combinationSum(c, t))
