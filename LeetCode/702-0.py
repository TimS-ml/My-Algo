'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

You can call ArrayReader.get(i) that:
returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]),
or returns 2^31 - 1 if the i is out of the boundary of the array.
'''

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        if reader.get(0) == target:
            return 0

        # search boundaries
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1  # right start with 1, so = r ** 2 won't work

        # binary search
        while left <= right:
            pivot = left + ((right - left) >> 1)
            num = reader.get(pivot)

            if num == target:
                return pivot
            if num > target:
                right = pivot - 1
            else:
                left = pivot + 1

        # there is no target element
        return -1
