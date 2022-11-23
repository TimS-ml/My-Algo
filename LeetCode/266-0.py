'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

import collections


class Solution:
    def canPermutePalindrome(self, s):
        calc = dict(collections.Counter(s))

        once = False
        for i in calc.values():
            if i % 2 == 1:
                if once:
                    return False
                once = True
        return True

    def canPermutePalindrome_2(self, s):
        return sum(v % 2 for v in collections.Counter(s).values()) < 2

    def canPermutePalindrome_3(self, s):
        sets = set()
        for char in s:
            if char not in sets:
                sets.add(char)
            else:
                sets.remove(char)

        return (len(sets) <= 1)

s = "carerac"
print(Solution().canPermutePalindrome(s))
