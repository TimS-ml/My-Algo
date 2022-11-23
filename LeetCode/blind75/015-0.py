'''
def twoSum(nums, target):
    # n1 + n2 == target
    return [n1, n2]

for i in range(len(nums)):
    n0 = -nums[i]
    # find n1 and n2 in nums[i+1:]

    # remove dupl
    # nums [0, 0, 0], [-1, -1, 2]
'''

class Solution:
    # TLE
    def threeSum(self, nums):
        # find all two sum !!!!!!
        def twoSum(idx, t):
            dic = {}  # val: idx
            ans = []
            for i in range(idx, len(nums)):
                if t - nums[i] in dic:
                    n1, n2 = t-nums[i], nums[i]
                    tmp = sorted([n1, n2])
                    if tmp not in ans:
                        ans.append(tmp)
                dic[nums[i]] = i
            return ans

        ans = []
        for i in range(len(nums)-2):
            n0 = nums[i]
            li = twoSum(i+1, -n0)
            # print(n0, n1, n2)
            if len(li) > 0:
                for n1n2 in li:
                    tmp = sorted([n0] + n1n2)
                    if tmp not in ans:
                        ans.append(tmp)

        return ans


nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))

