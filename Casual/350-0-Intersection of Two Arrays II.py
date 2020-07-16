# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans.append(nums1[i])
                nums2.remove(nums1[i])
        return ans


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
nums3 = [4, 9, 5]
nums4 = [9, 4, 9, 8, 4]

print(Solution().intersect(nums1, nums2))
print(Solution().intersect(nums3, nums4))
