'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)  # ok, not O(1)

'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1

        for k, v in dic.items():
            if v == 1:
                return k
        return -1
