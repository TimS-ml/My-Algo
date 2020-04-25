# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/

import collections


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = collections.Counter(nums1)
        print(type(dic), dic)

        ans = []
        for n in nums2:
            if dic[n] > 0:  # this is sorter than dic version
                # ans.append(n)
                ans += n,  # means ans += (num,)
                dic[n] -= 1
        return ans


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
nums3 = [4, 9, 5]
nums4 = [9, 4, 9, 8, 4]

print(Solution().intersect(nums1, nums2))
print(Solution().intersect(nums3, nums4))
