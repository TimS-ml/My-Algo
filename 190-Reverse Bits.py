# https://leetcode-cn.com/problems/reverse-bits/


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        mask = 1
        for _ in range(32):
            ans <<= 1
            print(bin(n), bin(ans))
            if mask & n:  # 按位从低到高，最后一位是1
                print('y')
                ans |= 1  # 给最后一位补1
            n >>= 1  # 抹掉n的最后一位
        return ans


n = 4294967293
print(Solution().reverseBits(n))

