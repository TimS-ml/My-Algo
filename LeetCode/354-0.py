'''
# Code Explain:
- Time complexity: O(NlogN)
- Space complexity: O(N)

'''

from bisect import bisect_left

class Solution:
    # dp + binary search
    def maxEnvelopes(self, arr: List[List[int]]) -> int:
        # sort increasing in first dimension and decreasing on second
        arr.sort(key=lambda x: (x[0], -x[1]))

        dp = []
        for _, height in arr:
            idx = bisect_left(dp, height)
            if idx == len(dp):
                dp.append(height)
            else:
                dp[idx] = height

        return len(dp)

    # dp
    def maxEnvelopes_2(self, envelopes: List[List[int]]) -> int:
        '''
        Since we have sorted width in increasing order, it is already increasing. 
        So we do not need to LIS in width as it is handled by sorting. 
        But the heights are non-increasingly sorted, so there we need to check for LIS
        '''
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        LIS = []
        size = 0
        for (w, h) in envelopes:
            if not LIS or h > LIS[-1]:
                LIS.append(h)
                size += 1
            else:
                l, r = 0, size
                while l < r:
                    m = l + (r - l) // 2
                    if LIS[m] < h:
                        l = m + 1
                    else:
                        r = m
                LIS[l] = h
        return size
