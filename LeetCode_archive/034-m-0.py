'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(1)

'''

class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
        if not nums:
            return [-1, -1]

        ans = []

        # [l, r]
        l,r = 0, len(nums) -1

        # left bound
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > t:
                # l side
                r = mid - 1
            elif nums[mid] < t:
                # r side
                l = mid + 1
            else:
                r = mid - 1

        # check l
        if l >= len(nums) or nums[l] != t:
            l = -1
        ans.append(l)


        # [l, r]
        l,r = 0, len(nums) -1

        # right bound
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > t:
                # l side
                r = mid - 1
            elif nums[mid] < t:
                # r side
                l = mid + 1
            else:
                l = mid + 1

        # check r
        if r < 0 or nums[r] != t:
            r = -1
        ans.append(r)

        return ans
