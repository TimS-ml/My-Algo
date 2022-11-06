'''
loop through nums
total sum S

case: if multiple 0 in nums
out: [0, ...]

case: if 1 0 in nums
out: [0, ..., val, ....]
val is at 0's position

'''

class Solution:
    def productExceptSelf(self, nums):
        S = 1
        zeroIdx = []

        for i in range(len(nums)):
            if nums[i] != 0:
                S *= nums[i]
            elif len(zeroIdx) == 0:
                zeroIdx.append(i)
                continue
            else:
                zeroIdx.append(i)
                break
        
        ans = []
        if len(zeroIdx) > 1:
            ans = [0 for _ in nums]
        elif len(zeroIdx) == 1:
            ans = [0 for _ in nums]
            ans[zeroIdx[0]] = S
        else:
            ans = [int(S/n) for n in nums]
        return ans


nums = [0,1,2,3]
print(Solution().productExceptSelf(nums))

