# https://leetcode-cn.com/problems/sliding-window-maximum/


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        dq = deque()
        res = []
        for i in range(len(nums)):
            # let window size <= k
            if dq and dq[0] == i - k:
                dq.popleft()
            # if new adding >= end number, pop end
            while dq and nums[i] >= nums[dq[-1]]:
                # print(nums[i], nums[dq[-1]])
                dq.pop()
            dq.append(i)
            if i - k + 1 >= 0:
                res.append(nums[dq[0]])
            print(dq, i, res)
        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
