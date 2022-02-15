'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



https://leetcode-cn.com/problems/contiguous-array/solution/python-qian-zhui-he-bian-liang-zi-dian-b-9oct/

001000[0011]00
  |  |      |
 diff=1   diff=1
which means [0011]'s diff=0

'''


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0: -1}
        diff, ans = 0, 0

        for idx, n in enumerate(nums):
            delta = 1 if n == 0 else -1
            diff += delta
            if diff in hashmap:
                ans = max(ans, idx - hashmap[diff])
            else:
                hashmap[diff] = idx

        return ans
