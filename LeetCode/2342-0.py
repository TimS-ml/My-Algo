'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from collections import defaultdict
from heapq import heappush, heappop


class Solution:

    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        ans = -1
        for num in nums:
            s = sum([int(digit) for digit in str(num)])
            if s not in dic:
                dic[s] = num
            else:
                ans = max(ans, dic[s] + num)
                dic[s] = max(dic[s], num)
        return ans

    # a correct way to maintain the sorted candidates
    def maximumSum_2(self, nums: List[int]) -> int:
        d, ans = defaultdict(list), -1

        # sum-of-digits function
        digits = lambda x: sum(map(int, list(str(x))))  
        for n in nums:  # construct max-heaps
            heappush(d[digits(n)], -n)

        for i in d:  # <-- pop the two greatest values off
            if len(d[i]) > 1:  #     each maxheap (when possible) and
                ans = max(ans, -heappop(d[i]) -
                          heappop(d[i]))  #     compare with current max value.

        return ans
