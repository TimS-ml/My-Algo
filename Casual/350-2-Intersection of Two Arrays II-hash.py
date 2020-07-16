# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        for n in nums1:
            dic[n] = dic.get(n, 0) + 1

        ans = []
        for n in nums2:
            if n in dic and dic[n] > 0:
                ans.append(n)
                dic[n] -= 1
        return ans


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
nums3 = [4, 9, 5]
nums4 = [9, 4, 9, 8, 4]

print(Solution().intersect(nums1, nums2))
print(Solution().intersect(nums3, nums4))
