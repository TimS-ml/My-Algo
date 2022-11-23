'''
# Code Explain:
- Time complexity: O(m*n)
    If give strings have length m and n
- Space complexity: O(m+n)

case 1:
   123 <-num1
*   45 <-num2
-------
    15
   10|
   5 |
   12| <- ans[0+1], carry = 1
   8 | <- ans[i+j] = num1[i] * num2[j]
  4  |
 43210

# Pros and Cons:
## Pros:

## Cons:

# Notation:
It's always a good practice to reverse the string first, so that you could start calculation from left to right.
'''


class Solution:
    def multiply(self, num1, num2):
        ans = [0] * (len(num1) + len(num2))  # placeholder
        for i, e1 in enumerate(reversed(num1)):
            for j, e2 in enumerate(reversed(num2)):
                ans[i + j] += int(e1) * int(e2)
                ans[i + j + 1] += int(ans[i + j] / 10)
                ans[i + j] %= 10
        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()
        return ''.join(map(str, ans[::-1]))

    def multiply_1(self, num1, num2):
        li = []
        for i, e1 in enumerate(reversed(num1)):
            for j, e2 in enumerate(reversed(num2)):
                li.append(int(e1) * int(e2) * pow(10, i + j))
        return str(sum(li))


# inputs
IN = [('123', '45'), ('99', '9')]
useSet = 0
print(Solution().multiply_1(IN[useSet][0], IN[useSet][1]))
