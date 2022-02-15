'''
# Code Explain:
- Time complexity: O(n)
n is len(str)
- Space complexity: O()



- In a palindrome, only at most one character appears an odd number of times
    - pick the first odd number of times char
- use each character an even number of times to make them symmetrical according to the palindrome center
- if there are remaining characters, we can take out one more and use it as the center of the palindrome
'''

import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
