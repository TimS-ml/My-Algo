# https://leetcode-cn.com/problems/fizz-buzz/
# 这样速度会快

class Solution:
    def fizzBuzz(self, n):
        ans = []
        for i in range(1, n + 1):
            is_three = i % 3 == 0
            is_five = i % 5 == 0
            if is_three and is_five:
                ans.append('FizzBuzz')
            elif is_three:
                ans.append('Fizz')
            elif is_five:
                ans.append('Buzz')
            else:
                ans.append(str(i))
        return ans


ANS = Solution().fizzBuzz(15)
print(ANS)
