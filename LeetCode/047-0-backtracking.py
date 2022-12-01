'''
# Code Explain:
- Time complexity: O(N! / (N-k)!)
- Space complexity: O(N)

'''

from typing import List


class Solution:
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()

    #     def backtrack(subset, nums):
    #         if not nums:
    #             ans.append(subset[:])
    #             return
    #         for i in range(len(nums)):
    #             if i > 0 and nums[i - 1] == nums[i]:
    #                 continue
    #             subset.append(nums[i])
    #             # print('sub:{} {}, nums:{}, i:{}'.format(nums[:i], nums[i+1:], nums, i))
    #             backtrack(subset, nums[:i] + nums[i + 1:])
    #             subset.pop()

    #     ans = []
    #     backtrack([], nums)
    #     return ans

    # create a list to track if visited or not
    def permuteUnique_2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # this is new vs lc 46
        visited = [False for _ in nums]

        def backtrack(subset):
            if len(subset) == len(nums):
                ans.append(list(subset))

            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and \
                        not visited[i - 1]:  # not used is new compares to lc 46
                    continue

                subset.append(nums[i])
                visited[i] = True  # track visit
                backtrack(subset)
                visited[i] = False
                subset.pop()

        ans = []
        backtrack([])
        return ans


nums = [1, 1, 2]
print(Solution().permuteUnique_2(nums))
