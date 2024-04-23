'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

alphanumeric: en char + number
Using .isalnum() and .lower() to preprocessing string
Using two pointers or list reverse to check if is Palindrome
'''

import pytest

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = filter(lambda x: x.isalnum(), s)
        s = map(lambda x: x.lower(), s)
        s = list(s)
        return s == s[::-1]


@pytest.mark.parametrize(
    "test_input, expected",
    [("", True),
     ("A man, a plan, a canal: Panama", True),
     ("race a car", False)]
)

def test_func(test_input, expected):
    assert Solution().isPalindrome(test_input) == expected
