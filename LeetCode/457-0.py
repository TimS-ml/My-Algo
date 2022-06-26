'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

'''

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        L = len(nums)

        # need to go over all the elements
        for i in range(L):
            linkLength = 0
            j = i
            forward = nums[j] > 0
            while True:
                if (forward and nums[j] < 0) or (not forward and nums[j] > 0):
                    break
                nextj = (j + nums[j] + L) % L
                # break until we found first one
                if nextj == j:
                    break
                j = nextj
                linkLength += 1
                if linkLength > L:
                    return True
        return False
