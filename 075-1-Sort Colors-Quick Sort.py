# https://leetcode-cn.com/problems/sort-colors/
# http://jalan.space/leetcode-notebook/#/algorithm/sort/quick/?id=_75-sort-colors
# the address of 'nums' is variant in each recursive layers, see hex(id(nums))


class Solution:
    def sortColors(self, nums):
        if len(nums) < 2:
            return nums
        tmp = self.quick_sort(nums)
        for i in range(len(nums)):
            nums[i] = tmp[i]
        nums.append(tmp[-1])
        # print(nums, hex(id(nums)))
        # print(nums)

    def quick_sort(self, nums):
        if len(nums) < 2:
            return nums

        left, right = [], []
        mid = nums[len(nums) // 2]
        nums.remove(mid)
        # print(hex(id(nums)))

        for i in nums:
            if i >= mid:
                right.append(i)
            elif i < mid:
                left.append(i)
        nums = self.quick_sort(left) + [mid] + self.quick_sort(right)
        return nums


nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums)
print(nums)
