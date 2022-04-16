'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[-1] <= 0:
            return [x ** 2 for x in nums][::-1]
        
        if nums[0] >=0:
            return [x ** 2 for x in nums]
        
        pos, neg = -1, -1

        # find non neg
        for i in range(len(nums)):
            if nums[i] >= 0:
                pos = i
                neg = i-1
                break
        
        ans = []
        while pos < len(nums) or neg >= 0:
            if pos < len(nums) and neg >= 0:
                if abs(nums[neg]) <= nums[pos]:
                    ans.append(nums[neg] ** 2)
                    neg -= 1

                elif abs(nums[neg]) > nums[pos]:
                    ans.append(nums[pos] ** 2)
                    pos += 1
            elif pos < len(nums) or neg >= 0:
                if pos >= len(nums):
                    ans.append(nums[neg] ** 2)
                    neg -= 1

                elif neg < 0:
                    ans.append(nums[pos] ** 2)
                    pos += 1
            
        return ans


