'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:
- target len(str) must be divisor of the length of the two strings
- If there is a string X that meets the requirements, there must also be a string X' that meets the requirements
  - and its length is the greatest common divisor of the lengths of str1 and str2
  - math.gcd
'''

import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1), len(str2)), 0, -1):
            if (len(str1) % i) == 0 and (len(str2) % i) == 0:
                if str1[:i] * (len(str1) // i) == str1 and \
                   str1[:i] * (len(str2) // i) == str2:
                    return str1[:i]
        return ''

    def gcdOfStrings_2(self, str1: str, str2: str) -> str:
        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[:candidate_len]
        if candidate * (len(str1) // candidate_len) == str1 and \
           candidate * (len(str2) // candidate_len) == str2:
            return candidate
        return ''
