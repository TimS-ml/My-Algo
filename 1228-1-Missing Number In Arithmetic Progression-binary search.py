from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[-1] - arr[0]) // len(arr)
        if d == 0:
            return arr[0]
        left, right = 0, len(arr) - 1
        mid = (left + right) // 2
        while mid != left:
            if arr[mid] - arr[left] == (mid - left) * d:
                left = mid
            else:
                right = mid
            mid = (left + right) // 2
        return arr[mid] + d


arr1 = [5, 7, 11, 13]
arr2 = [5, 9, 11, 13]
arr3 = [5, 9, 11]
print(Solution().missingNumber(arr2))
