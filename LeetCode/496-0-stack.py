'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

'''


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        ans = []
        stack = []
        dic = dict()
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1]:
                dic[stack.pop()] = nums[i]
            stack.append(nums[i])  # nums[-1] will remain in stack after loop

        # deal with the remain element in stack
        # before: stack = [5] dic = {1: 3, 3: 4, 2: 5, 4: 5}
        # after : stack = []  dic = {1: 3, 3: 4, 2: 5, 4: 5, 5: -1}
        while stack:
            dic[stack.pop()] = -1

        for i in range(len(findNums)):
            ans.append(dic[findNums[i]])
        return ans


findNums = [4, 1, 2]
nums = [1, 3, 4, 2, 5]
