'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        # find index of peak
        l, r = 0, n - 1
        while l < r:
            m = int((l + r) / 2)
            if mountain_arr.get(m) < mountain_arr.get(m + 1):
                l = peak = m + 1
            else:
                r = m
        # find target in the left of peak
        l, r = 0, peak
        while l <= r:
            m = int((l + r) / 2)
            if mountain_arr.get(m) < target:
                l = m + 1
            elif mountain_arr.get(m) > target:
                r = m - 1
            else:
                return m
        # find target in the right of peak
        l, r = peak, n - 1
        while l <= r:
            m = int((l + r) / 2)
            if mountain_arr.get(m) > target:
                l = m + 1
            elif mountain_arr.get(m) < target:
                r = m - 1
            else:
                return m
        return -1
