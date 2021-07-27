# https://leetcode-cn.com/problems/rabbits-in-forest/
# https://leetcode.com/problems/rabbits-in-forest/discuss/114721/C%2B%2BJavaPython-Easy-and-Concise-Solution
# Count the res as we loop on the answers.

import collections


class Solution:
    def numRabbits(self, answers):
        c = collections.Counter()  # a new, empty counter
        res = 0
        for i in answers:
            print(c[i])
            if c[i] % (i + 1) == 0:
                res += i + 1
                print(c[i], i + 1, res)
            c[i] += 1
        return res


ans0 = []
ans1 = [10, 10, 10]
ans2 = [1, 1, 2]
ans3 = [0, 0, 1, 1, 1]
ans4 = [0, 1, 0, 2, 0, 1, 0, 2, 1, 1]
print(Solution().numRabbits(ans3))
