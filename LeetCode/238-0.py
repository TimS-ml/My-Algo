'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)

# Pros and Cons and Notation:
case: 0 in list
count_0 =0 or =1 or >1
'''

from typing import List


class Solution:
    # avoid divide by 0
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)
        nums.extend(nums)
        ans = []
        base = 1
        for i in range(L - 1):
            base *= nums[i]
        for i in range(L):
            if nums[i] != 0:
                base *= nums[i + L - 1] / nums[i]
                ans.append(int(base))
            else:
                temp = 1
                sublist = nums[:i] + nums[i + 1:]
                for j in range(L - 1):
                    temp *= sublist[j]
                ans.append(temp)
        return ans

    # L[i] = prod(nums[:i])
    # R[i] = prod(nums[i+1:])
    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        L = len(nums)
        L, R, ans = [0] * L, [0] * L, [0] * L

        L[0] = 1
        for i in range(1, L):
            L[i] = nums[i - 1] * L[i - 1]

        R[L - 1] = 1
        for i in reversed(range(L - 1)):
            R[i] = nums[i + 1] * R[i + 1]

        for i in range(L):
            ans[i] = L[i] * R[i]

        return ans


#  nums = [1, 2, 3, 4]
nums = [-1, 1, 0, -3, 3]
print(Solution().productExceptSelf(nums))
