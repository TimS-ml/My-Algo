# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
# 有越界的问题


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binarySearch(nums, target):
            start, end = 0, len(nums) - 1
            while start + 1 < end:
                mid = int(start + (end - start) / 2)
                if nums[mid] > target:
                    end = mid
                elif nums[mid] < target:
                    start = mid
                else:
                    return True
                if nums[start] == target:
                    return True
                if nums[end] == target:
                    return True
            return False

        for nums in matrix:
            if binarySearch(nums, target):
                return True
        return False


matrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
# matrix = [[-5]]

target = -5

print(Solution().searchMatrix(matrix, target))
