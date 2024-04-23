'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

import collections
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = collections.Counter(arr)
        return len(dic) == len(set(dic.values()))

