# https://leetcode-cn.com/problems/counting-bits/
# 对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回


class Solution:
    def countBits(self, num: int):
        if num == 0:
            return [0]
        ans = [0, 1]
        j = 0
        for i in range(2, num+1):
            ans.append(ans[i & (i-1)] + 1)
        return ans


num = 5
