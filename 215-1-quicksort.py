'''
# Thought process
[1] sort the list
  - easy way: nums.sort(reverse=True), time: O(N * log(N))
  - heapq in python: O(N * log(2N))
    - in python, heappop will pop minimum value
  - Merge Sort or Quick Sort: O(N * log(N))
[2] located the kth number
  - k start at 1

# Test cases
3,2,3,1,2,4,5,5,6
4

'''

from typing import List
import random
# from heapq import heapify, heappop, heappush


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k  # the index we gonna find
        left = 0
        right = len(nums) - 1
        while True:
            index = self.__partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                # find in [index+1, right]
                left = index + 1
            else:
                # find in [left, index-1]
                right = index - 1

    def __partition(self, nums, left, right):
        # random inin pivot to avoid extreme cases
        random_index = random.randint(left, right)
        nums[random_index], nums[left] = nums[left], nums[random_index]

        # loop, [left+1, right] < pivot and [j, i] >= pivot
        pivot = nums[left]
        j = left
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
        # put pivot in right position
        nums[left], nums[j] = nums[j], nums[left]
        return j


nums1 = [3, 2, 3, 1, 2, 4, 5, 5, 6]  # 4
k1 = 4

nums2 = [3, 2, 1, 5, 6, 4]  # 5
k2 = 2
print(Solution().findKthLargest(nums1, k1))
print(Solution().findKthLargest(nums2, k2))
