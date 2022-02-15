'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



'''

from typing import List
from functools import lru_cache


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        @lru_cache(None)
        # you cannot use the brute one with lambda...
        def countOne_brute(x):
            c = 0
            while x > 0:
                c += x % 2
                x /= 2
            return c

        def countOne(x):
            return bin(x).count('1')

        arr.sort(key=lambda e: (countOne(e), e))
        return arr
