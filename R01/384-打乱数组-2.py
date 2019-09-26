# https://leetcode-cn.com/problems/shuffle-an-array/
# Fisher–Yates shuffle

import random


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.init = list(nums)
        self.nums = nums
        self.length = len(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = list(self.init)
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in reversed(range(self.length)):
            index = random.randint(0, i)
            self.nums[i], self.nums[index] = self.nums[index], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()