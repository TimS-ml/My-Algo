'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans = 0
        for i, j in enumerate(sorted(citations, reverse=True)):
            if i < j:
                ans += 1

        return ans
