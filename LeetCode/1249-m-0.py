'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

- Counter doesn't work, order of ( and ) matters
- Eng letter: save location of ( and )

Solution:
- 1st loop: build a stack to determine which parenthesis to keep
- 2nd loop: generate output


- Build a stack (list) in python
- loop through the list(str)
    - when '(': append
    - when ')':
        if stack[-1] is (
        # if ( in stack
        #     remove )
        else  # stack empty or ) in stack
            append )

After looping:
- case1: (())  => empty
- case2: ())   => )
- case3: (()   => (
- case4: )(    => )(
- case5: )()   => )
'''

import pytest

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:


@pytest.mark.parametrize(
    "test_input, expected", 
    [
        ("lee(t(c)o)de)", {"lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"}),
        ("a)b(c)d", {"ab(c)d"}),
        ("))((", {""})
    ]
)

def test_func(test_input, expected):
    assert Solution().minRemoveToMakeValid(test_input) in expected
