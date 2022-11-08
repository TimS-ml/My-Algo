'''
s is palindrome:
- s == s[::-1]
- if s2 = s[x:-x], x <= len(s) // 2
    s2 is palindrom
- When l <= r:
    s[l] == s[r]
    l += 1
    r -= 1

del at most one:
- counter = 0
- counter <= 1
- When s[l] != s[r]:
    counter += 1  # should I move l or r ???

two pointers:
move to middle
s = "abca"
     |  |
     l  r

solution:
move l and r to middle
if s[l] != s[r]
    sl = s[l+1:r]
    sr = s[l:r-1]
    find if sl or sr is palindrom
'''

import pytest

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l <= r:
            if s[l] == s[r]:
                l += 1 
                r -= 1
            else:
                sl = s[l+1:r]
                sr = s[l:r-1]
                return sl == sl[::-1] or \
                        sr == sr[::-1]

        return True


# @pytest.fixture
# def tester(request):
#     """Create tester object"""
#     return Solution(request.param)


@pytest.mark.parametrize(
    "test_input, expected", 
    [("", True),
     ("a", True),
     ("abobca", True),
     ("aaa", True),
     ("abc",False),
     ("abab",False)]
)

def test_func(test_input, expected):
    assert Solution().validPalindrome(test_input) == expected

pytest.main()

