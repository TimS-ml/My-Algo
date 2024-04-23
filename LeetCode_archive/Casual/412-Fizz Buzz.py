# https://leetcode-cn.com/problems/fizz-buzz/


class Solution:
    def fizzBuzz(self, n):
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')
            elif i % 3 == 0:
                ans.append('Fizz')
            elif i % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(i))
        return ans


ANS = Solution().fizzBuzz(15)
print(ANS)
