'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons:
https://en.wikipedia.org/wiki/Bitwise_operation
- 按位与(&): 如果两个二进位都为1, 则该位结果为1, 否则为0
- 按位或(|): 只要一个为1, 则为1, 否则为0
- 按位异或(^): 两个二进位相异为为1(即两个二进位要相反), 否则为0
- 取反/补码(~): 对数据的每个二进制位取反, 即把1变0, 把0变1

first = arr[0]
arr[i+1] = encoded[i] XOR arr[i]
'''

from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for a in encoded:
            first ^= a
            ans.append(first)
        return ans
