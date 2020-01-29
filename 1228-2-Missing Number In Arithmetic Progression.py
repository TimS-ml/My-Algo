from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return (arr[0] + arr[-1]) * (len(arr) + 1) // 2 - sum(arr)


arr1 = [5, 7, 11, 13]
arr2 = [5, 9, 11, 13]
arr3 = [5, 9, 11]
print(Solution().missingNumber(arr2))
