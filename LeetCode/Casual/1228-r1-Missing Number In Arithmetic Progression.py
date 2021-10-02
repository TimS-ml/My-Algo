from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[-1] - arr[0]) / len(arr)
        if d == 0:
            return 0
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] != d:
                return int(arr[i] + d)


arr1 = [5, 7, 11, 13]
arr2 = [5, 9, 11, 13]
arr3 = [5, 9, 11]
arr4 = [0, 0, 0, 0]
print(Solution().missingNumber(arr2))
