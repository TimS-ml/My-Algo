'''
# Code Explain:
- Time complexity: O(1)  # suppose it's a 32bit binary, then while loop <= 32 times
- Space complexity: O(1)

n is int, but we need to count '1' in bit format

'&': only 1 + 1 return 1, else 0

remove last '1' in n
n -= (n & -n)
n = n & (n - 1)
'''


class Solution(object):
    def print_bin(self, n: int, dig: int = 16):
        assert n > 0
        print('pos: ', bin(n))
        print('n-1: ', bin(n-1))
        print('neg: ', bin((1 << dig) - abs(n)))
        print('inv: ', bin((1 << dig) - abs(~n)))  # diff 1 with neg
        print('n & -n : ', bin(n & -n))       # keep only the last '1', thus we need n -= (n & -n)
        print('n & n-1: ', bin(n & (n - 1)))  # remove the last '1'
        print()

    def hammingWeight(self, n):
        ans = 0
        while n > 0:
            self.print_bin(n)
            # n -= (n & -n)
            n = n & (n - 1)
            ans += 1
        return ans


inpute = '00000000000000000000000000001011'
n = int(inpute)
print(n)
print(Solution().hammingWeight(n))
