'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

import collections
from typing import List


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # ans = []
        # nums1.sort()
        # nums2.sort()
        # i = j = 0
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     elif nums1[i] > nums2[j]:
        #         j += 1
        #     else:
        #         ans.append(nums1[i])
        #         i += 1
        #         j += 1
        # return ans

        ans = []
        nums1.sort()
        nums2.sort()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans.append(nums1[i])
                nums2.remove(nums1[i])
        return ans

    def intersect2(self, nums1, nums2):
        dic = {}
        for n in nums1:
            dic[n] = dic.get(n, 0) + 1

        ans = []
        for n in nums2:
            if n in dic and dic[n] > 0:
                ans.append(n)
                dic[n] -= 1
        return ans

    def intersect3(self, nums1, nums2):
        dic = collections.Counter(nums1)
        # print(type(dic), dic)

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
