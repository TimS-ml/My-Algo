'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(start, substr):
            self.ans = max(len(substr), self.ans)
            if start == len(arr):
                return
            for i in range(start, len(arr)):
                if not len(substr+arr[i]) > len(set(substr+arr[i])):
                    print("before", i, substr)
                    backtrack(i+1, substr+arr[i])
                    print("after", i+1, substr)
        self.ans = 0  # the max len
        backtrack(0, "")
        return self.ans


# inputs
arr = ["un","iq","ue"]
print(Solution().maxLength(arr))

