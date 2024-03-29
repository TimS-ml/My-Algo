'''
# Code Explain:
- Time complexity: O(N * N!)
- Space complexity: O(N)

nums[:i] + nums[i+1:] will give us
- a list without nums[i]
- avoid generate temp variable

'''


class Solution:
    # this is not universal solution
    def permute(self, nums):
        # `start` only applies for non-dupl nums
        def backtrack(start):
            if start == n:
                ans.append(nums[:])
            for i in range(start, n):
                # place i-th integer start
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                # reverse movement
                nums[start], nums[i] = nums[i], nums[start]

        n = len(nums)
        ans = []
        backtrack(0)
        return ans

    # in lc 047 (duplication), add a var 'used'
    # from joshuablog
    def permute_2(self, nums):
        def backtrack(subset):
            # at leaf
            if len(subset) == len(nums):
                ans.append(subset[:])
                return
            for i in range(len(nums)):
                # only applies for non-dupl nums
                if nums[i] in subset:
                    continue
                subset.append(nums[i])
                backtrack(subset)
                # reverse movement
                subset.pop()

        ans = []
        backtrack([])
        return ans

    def permute_3(self, nums):
        visited = [False for _ in nums]

        def backtrack(subset):
            # collect perm of size of len(nums)
            if len(subset) == len(nums):
                ans.append(subset[:])
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue

                visited[i] = True
                subset.append(nums[i])
                backtrack(subset)
                subset.pop()
                visited[i] = False
        ans = []
        backtrack([])
        return ans


nums = [1, 2, 3]
print(Solution().permute(nums))
