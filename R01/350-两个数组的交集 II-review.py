# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/


class Solution:
    def intersect(self, nums1, nums2) -> List[int]:
        ans = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
nums3 = [4,9,5]
nums4 = [9,4,9,8,4]

print(Solution().intersect(nums1, nums2))
print(Solution().intersect(nums3, nums4))