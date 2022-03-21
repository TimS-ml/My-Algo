'''
# Code Explain:
- Time complexity: O(N logN)
- Space complexity: O(n)

https://docs.python.org/3/library/functools.html#functools.cmp_to_key
https://www.programiz.com/python-programming/methods/built-in/sorted

We need reverse order, be careful with the cmp function

If:
A concat B > B concat C
B concat C > C concat A

Then:
A concat C > C concat A

Is that correct: number start with 9 should be placed first. => NO

case:
aStr := "3" + "30" = "330"
bStr := "30" + "3" = "303"
'''

from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(y + x) - int(x + y)

        li = map(str, nums)
        li = sorted(li, key=cmp_to_key(compare))
        if li[0] == '0':
            return '0'
        else:
            return ''.join(li)

    def largestNumber_2(self, nums: List[int]) -> str:
        compare = lambda x, y: 1 if x + y < y + x else -1
        li = map(str, nums)
        li = sorted(li, key=cmp_to_key(compare))
        if li[0] == '0':
            return '0'
        else:
            return ''.join(li)


nums = [3, 30, 34, 5, 9]
print(Solution().largestNumber_2(nums))
