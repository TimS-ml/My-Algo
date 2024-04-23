'''
# Code Explain:
- Time complexity: O(M + N) where M and N are the length of n1 and n2
- Space complexity: O(M + N)
'''


class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)

    def intersection2(self, nums1, nums2):
        def set_intersection(self, set1, set2):
            return [x for x in set1 if x in set2]

        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return set_intersection(set1, set2)
        else:
            return set_intersection(set2, set1)
