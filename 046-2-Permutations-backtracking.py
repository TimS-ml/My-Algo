# https://leetcode-cn.com/problems/permutations/
# a faster version


class Solution:
    def permute(self, nums):
        def backtrack(first = 0):
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # print(first)
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output


nums = [1, 2, 3]
print(Solution().permute(nums))
