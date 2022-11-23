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
- case6: ())()((( => )(((

After s.remove:
- case1: (())  => (())
- case2: (l)c) => (lc)
- case3: (l(c) => l(c)
- case4: )(    => )(
- case5: )()   => )
- case6: ())()((( => ())(


# Feedback
This is wrong
You should save idx of what parentheses needed to be remove
Next time use stack + save idx, it's easier

How to find unmatched left parentheses  (count > 0)? Remove fist appearance is wrong
    case: ( () (, delete 1st and 3rd
    https://youtu.be/U1nwBAIQ-oc?t=420
How to find unmatched right parentheses (count < 0)? Remove directly
'''

import pytest

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:  # empty or ')'
                    stack.append(s[i])

        for i in range(len(stack)):
            s.remove(stack[i])  # remove the first appearance

        return ''.join(s)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("lee(t(c)o)de)", {"lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"}),
        ("a)b(c)d", {"ab(c)d"}),
        ("))((", {""}),
        ("())()(((", {"()()"})  # failed
    ]
)

def test_func(test_input, expected):
    assert Solution().minRemoveToMakeValid(test_input) in expected
