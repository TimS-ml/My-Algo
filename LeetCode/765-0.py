'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:
x 的对象是x ^ 1
- 当 x 是偶数, 则其二进制的末尾是 0, 所以 x ^ 1 将其二进制的末尾改成 1, 于是得到了x的对象 x + 1
- 当 x 是奇数, 则其二进制的末尾是 1, 所以 x ^ 1 将其二进制的末尾改成 0, 于是得到了x的对象 x - 1
'''

from typing import List


class Solution(object):
    # time: O(n^2)
    # case: [0,2,1,3]
    # middle: [0, 2, 2, 3] {0: 0, 2: 2, 1: 2, 3: 3}
    def minSwapsCouples_greedy(self, row: List[int]) -> int:
        L = len(row)
        dic = {}
        ans = 0
        for i in range(L):
            dic[row[i]] = i

        # step = 2
        for i in range(0, L - 1, 2):
            if row[i] == row[i + 1] ^ 1:
                continue

            # copy val from i + 1 to original couple's position + update dic
            # no need to swap value
            row[dic[row[i] ^ 1]] = row[i + 1]
            dic[row[i + 1]] = dic[row[i] ^ 1]
            # for j in range(i + 1, L):
            #     if row[i] == row[j] ^ 1:
            #         row[i + 1], row[j] = row[j], row[i + 1]
            ans += 1
        return ans

    def minSwapsCouples(self, row: List[int]) -> int:
        return
