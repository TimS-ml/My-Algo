'''
# Code Explain:
Let N be the length of the input array and L1, L2 be the number of non-zero elements.

Sol 1
Init
- Time complexity: O(N)
- Space complexity: O(L)

Dot (v1.dot(v2))
- Time complexity: O(L1)
- Space complexity: O(1)

Sol 1
Init
- Time complexity: O(N)
- Space complexity: O(L)

Dot (v1.dot(v2))
- Time complexity: O(L1 + L2)
- Space complexity: O(1)
'''

# hash dic
# index val pairs
class SparseVector:
    def __init__(self, nums: List[int]):
        self.dic = {}
        for k, v in enumerate(nums):
            if v != 0:
                self.dic[k] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # self.dic and vec.dic
        ans = 0
        for k1, v1 in self.dic.items():
            if k1 in vec.dic:
                ans += self.dic[k1] * vec.dic[k1]
        return ans

# 2 pointers
# index val pairs
class SparseVector_2:
    def __init__(self, nums: List[int]):
        self.dic = []  # 2-d list
        for k, v in enumerate(nums):
            if v != 0:
                self.dic.append([k, v])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # self.dic and vec.dic
        ans = 0
        p, q = 0, 0

        while p < len(self.dic) and q < len(vec.dic):
            if self.dic[p][0] == vec.dic[q][0]:
                ans += self.dic[p][1] * vec.dic[q][1]
                p += 1
                q += 1
            elif self.dic[p][0] < vec.dic[q][0]:
                p += 1
            else:
                q += 1
        return ans

# index val pairs
class SparseVector_3:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1

        return result


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
