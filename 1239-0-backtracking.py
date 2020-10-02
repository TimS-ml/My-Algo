'''
# Code Explain:
- Time complexity: O(N!)
- Space complexity: O()

# Pros and Cons:
## Pros:

## Cons:

# Notation:
go through all the possibility by `start` and `i`
'''

from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(start, substr):
            self.ans = max(len(substr), self.ans)
            for i in range(start, len(arr)):
                if not len(substr + arr[i]) > len(set(substr + arr[i])):
                    print("before", i, substr)
                    backtrack(i + 1, substr + arr[i])
                    print("after", i + 1, substr)

        self.ans = 0  # the max len
        backtrack(0, "")
        return self.ans

    def maxLength2(self, arr: List[str]) -> int:
        def backtrack(start, substr):  # substr may not be legal case
            if len(substr) == len(set(substr)):
                self.ans = max(len(substr), self.ans)
            for i in range(start, len(arr)):
                if len(substr) > len(set(substr)):
                    break
                print("before", i, substr)
                backtrack(i + 1, substr + arr[i])
                print("after", i + 1, substr)

        self.ans = 0  # the max len
        backtrack(0, "")
        return self.ans


# inputs
# arr = ["un","iq","ue"]
# arr = ["cha","r","act","ers"]
arr = [
    "abcdefghijklm", "bcdefghijklmn", "cdefghijklmno", "defghijklmnop",
    "efghijklmnopq", "fghijklmnopqr", "ghijklmnopqrs", "hijklmnopqrst",
    "ijklmnopqrstu", "jklmnopqrstuv", "klmnopqrstuvw", "lmnopqrstuvwx",
    "mnopqrstuvwxy", "nopqrstuvwxyz", "opqrstuvwxyza", "pqrstuvwxyzab"
]
print(Solution().maxLength2(arr))
