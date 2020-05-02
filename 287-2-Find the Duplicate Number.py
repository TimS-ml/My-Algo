# https://leetcode-cn.com/problems/find-the-duplicate-number/
# https://leetcode-.com/problems/find-the-duplicate-number/solution/xun-zhao-zhong-fu-shu-by-leetcode/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1


nums = [1, 2, 2, 3, 4]
print(Solution().findDuplicate(nums))

