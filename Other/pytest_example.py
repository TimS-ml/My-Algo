'''
lc 680
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
                sl = s[l+1:r+1]
                sr = s[l:r]
                return sl == sl[::-1] or \
                        sr == sr[::-1]

        return True


# @pytest.fixture
# def tester(request):
#     """Create tester object"""
#     return Solution(request.param)


# This is a decorator!!!
@pytest.mark.parametrize(
    "test_input, expected", 
    [("", True)]
)
def test_dege(test_input, expected):
    assert Solution().validPalindrome(test_input) == expected

@pytest.mark.parametrize(
    "test_input, expected", 
    [("a", True),
     ("aaa", True)]
)
def test_valid(test_input, expected):
    assert Solution().validPalindrome(test_input) == expected

@pytest.mark.parametrize(
    "test_input, expected", 
    [("abobca", True),
     ("abab", True),
     ("abc", False)]
)
def test_valid_after_Del(test_input, expected):
    assert Solution().validPalindrome(test_input) == expected

pytest.main()

