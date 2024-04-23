'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

cnt: it's 2-dig loop (solution 1)
ref: forward n dig reference + 1 (solution 2)

 cnt                2^0 2^1 2^2 2^3 2^4 ref
  0        0   =  0  0                     
  1        1   =  1  1                   1 
  1 + '0'  2+0 =  2  0   1               1 
  1 + '1'  2+1 =  3  1   1               2 
           
  1 + '0'  4+0 =  4  0   0   1           2 
  1 + '1'  4+1 =  5  1   0   1           4 
  1 + '2'  4+2 =  6  0   1   1           4 
  1 + '3'  4+3 =  7  1   1   1           4 
           
  1 + '0'  8+0 =  8  0   0   0   1       4 
  1 + '1'  8+1 =  9  1   0   0   1       8 
  1 + '2'  8+2 = 10  0   1   0   1       8 
  1 + '3'  8+3 = 11  1   1   0   1       8 
           
  2 + '0'  8+4+0 = 12       ...          8 
  2 + '1'  8+4+1 = 13       ...          8 
  2 + '2'  8+4+2 = 14       ...          8 
  2 + '3'  8+4+3 = 15       ...          8 
'''

def eda(n = 16):
    for i in range(n + 1):
        print(i, bin(i))


class Solution:
    # using 191's solution
    def countBits(self, n: int):
        def singleCount(n):
            dp = 0
            while n > 0:
                n = n & (n - 1)
                dp += 1
            return dp
        
        return [singleCount(i) for i in range(n + 1)]

    # def countBits(self, n: int):
    #     if n == 0:
    #         return [0]
    #     dp = [0, 1]

    #     for i in range(2, n + 1):
    #         print(i & (i - 1))  # use this trick to remove the last '1'
    #         dp.append(dp[i & (i - 1)] + 1)
    #     return dp

    def countBits_a(self, n: int):
        '''dp[x] = dp[x & (x - 1)] + 1
        '''
        dp = [0] * (n + 1)
        for x in range(1, n + 1):
            dp[x] = dp[x & (x - 1)] + 1
        return dp 

    def countBits_b(self, n: int):
        '''dp[x] = dp[x / 2] + (x mod 2)
        '''
        dp = [0] * (n + 1)
        for x in range(1, n + 1):
            # x // 2 is x >> 1 and x % 2 is x & 1
            dp[x] = dp[x >> 1] + (x & 1) 
        return dp 

    def countBits_2a(self, n: int):
        '''dp[x + b] = dp[x] + 1, b = 2^m > x
        '''
        dp = [0] * (n + 1)
        x = 0
        b = 1
        
        # [0, b) is calculated
        while b <= n:
            # generate [b, 2b) or [b, n) from [0, b)
            while x < b and x + b <= n:
                dp[x + b] = dp[x] + 1
                x += 1
            x = 0 # reset x
            b <<= 1 # b = 2b
        return dp

    def countBits_2b(self, n: int):
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            print(f'{i:02d}, {offset:02d}, i-offset: {i - offset}')
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp 


# eda()
n = 15
# print(Solution().countBits(n))
print(Solution().countBits_2b(n))
