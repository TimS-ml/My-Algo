'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)

# Thoughts:
s is palindrome:
- s == s[::-1]
- if s2 = s[x:-x], x <= len(s) // 2
    s2 is palindrom
- When l <= r:
    s[l] == s[r]
    l += 1
    r -= 1

del at most one:
- When s[l] != s[r]:
    counter += 1  # should I move l or r ???


two pointers:
move to middle
s = "abca"
     |  |
     l  r

# Solution:
move l and r to middle
if s[l] != s[r]
    sl = s[l+1:r]
    sr = s[l:r-1]
    find if sl or sr is palindrom


# Follow up:
del at most n:
- counter = 0
- counter <= 1
- tree structure
'''

import pytest

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                sl = s[l+1:r+1]
                sr = s[l:r]
                # print(sl, sr)
                return sl == sl[::-1] or \
                        sr == sr[::-1]

        return True

    def validPalindrome_2(self, s: str) -> bool:
        def isPalindrome(l, r, s, d=1):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if d > 0:
                        return isPalindrome(l+1, r, s, d-1) or isPalindrome(l, r-1, s, d-1)
                    else:
                        return False
            return True

        return isPalindrome(0, len(s)-1, s, 1)


@pytest.mark.parametrize(
    "test_input, expected",
    [("", True),
     ("a", True),
     ("abobca", True),
     ("aaa", True),
     ("abc", False),
     ("abab", True)]
)

def test_func(test_input, expected):
    assert Solution().validPalindrome_2(test_input) == expected

# pytest.main()
