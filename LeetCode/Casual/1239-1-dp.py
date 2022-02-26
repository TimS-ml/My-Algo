'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

[1] Base State
dp[substr] = len of substr

[2] State Transfer Equation
dp[word + v] = max(dp[word + v], len(word + v))
this is defaultdict, so dp[sth new] = 0

[3] Initialize Conditions
dp[''] = 0

[4] State Compression (optional)
no

[5] Terminate Conditions
for each word in arr, go through all dict
    create word + dict combinations

# Pros and Cons:
## Pros:

## Cons:

# Notation:
go through all the possibility by `start` and `i`
'''

from typing import List
import collections


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = collections.defaultdict(int)
        dp[''] = 0
        for word in arr:
            for v in list(dp.keys()):
                # if not valid element in arr
                if len(word) != len(set(word)):
                    break
                if len(word + v) == len(set(word + v)):
                    dp[word + v] = max(dp[word + v], len(word + v))
        return max(dp.values())


# inputs
# arr = ["un", "iq", "ue"]
# arr = ["cha", "r", "act", "ers"]
arr = [
    "abcdefghijklm", "bcdefghijklmn", "cdefghijklmno", "defghijklmnop",
    "efghijklmnopq", "fghijklmnopqr", "ghijklmnopqrs", "hijklmnopqrst",
    "ijklmnopqrstu", "jklmnopqrstuv", "klmnopqrstuvw", "lmnopqrstuvwx",
    "mnopqrstuvwxy", "nopqrstuvwxyz", "opqrstuvwxyza", "pqrstuvwxyzab"
]
print(Solution().maxLength(arr))
