# https://leetcode-cn.com/problems/find-lucky-integer-in-an-array/

from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        dic = Counter(arr)
        for i in dic:
            if dic[i] == i:
               ans = max(ans, i) 
        return ans


arr = [2, 2, 3, 4]
# arr = [1, 2, 2, 3, 3, 3]
print(Solution().findLucky(arr))

