'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

# hash dic
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

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
