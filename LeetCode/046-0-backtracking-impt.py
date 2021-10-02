'''
# Code Explain:
- Time complexity: O(N * N!)
- Space complexity: O(N)

nums[:i] + nums[i+1:] will give us
- a list without nums[i]
- avoid generate temp variable

Also, check `046.png`
sub:[] [2, 3], nums:[1, 2, 3], i:0
sub:[] [3], nums:[2, 3], i:0
sub:[] [], nums:[3], i:0
sub:[2] [], nums:[2, 3], i:1
sub:[] [], nums:[2], i:0
sub:[1] [3], nums:[1, 2, 3], i:1
sub:[] [3], nums:[1, 3], i:0
sub:[] [], nums:[3], i:0
sub:[1] [], nums:[1, 3], i:1
sub:[] [], nums:[1], i:0
sub:[1, 2] [], nums:[1, 2, 3], i:2
sub:[] [2], nums:[1, 2], i:0
sub:[] [], nums:[2], i:0
sub:[1] [], nums:[1, 2], i:1
sub:[] [], nums:[1], i:0

# Pros and Cons:
## Pros:

## Cons:

# Notation:
LC077 / 078
'''


class Solution:
    # this is not universal solution
    def permute(self, nums):
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
            if len(nums) == len(subset):
                ans.append(subset[:])
                return
            for i in range(len(nums)):
                if nums[i] in subset:
                    continue
                subset.append(nums[i])
                backtrack(subset)
                # reverse movement
                subset.pop()

        ans = []
        backtrack([])
        return ans

    # yet another way to avoid duplicate
    def permute_3(self, nums):
        def backtrack(subset, nums):
            if not nums:
                ans.append(subset[:])
                return
            for i in range(len(nums)):
                subset.append(nums[i])
                # print('sub:{} {}, nums:{}, i:{}'.format(
                #     nums[:i], nums[i + 1:], nums, i))
                backtrack(subset, nums[:i] + nums[i + 1:])
                subset.pop()

        ans = []
        backtrack([], nums)
        return ans


nums = [1, 2, 3]
print(Solution().permute(nums))
