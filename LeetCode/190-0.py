'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


class Solution:
    def reverseBits(self, n):
        ans = 0
        mask = 1
        for _ in range(32):
            ans <<= 1
            print(bin(n), bin(ans))
            if mask & n:  # if last dig of 'n' is 1
                ans |= 1  # make the last dig of ans 1 
            n >>= 1
        return ans

    # a better way
    def reverseBits_2(self, n: int) -> int:
        ans = 0
        for i in range(32):
            bit = (n >> i) & 1
            ans += (bit << (31 - i))
        return ans

    # http://graphics.stanford.edu/~seander/bithacks.html#ReverseByteWith64BitsDiv
    def reverseBits_3(self, n):
        ans, power = 0, 24
        cache = dict()
        while n:
            ans += self.reverseByte(n & 0xff, cache) << power
            n = n >> 8
            power -= 8
        return ans

    def reverseByte(self, byte, cache):
        if byte not in cache:
            cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023 
        return cache[byte]


n = 4294967293
print(Solution().reverseBits(n))
