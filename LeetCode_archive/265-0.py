'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

find the min index such that citations[i] >= len(citations) - i
'''

class Solution:
    # left bound
    def hIndex(self, citations):
        if not citations:
            return 0
        if citations == [0]:
            return 0
        
        n = len(citations)
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            # smaller mid
            if citations[mid] == n - mid:
                # return n - mid
                r = mid
            elif citations[mid] < n - mid:
                l = mid + 1
            elif citations[mid] > n - mid:
                r = mid
        return n - l
