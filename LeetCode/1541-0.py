'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Example
(()))) => balanced
(())()))) = 
    (
        ()) ())
    )) => balanced


# Explanation
res represents the number of left/right parentheses already added.
right represents the number of right parentheses needed.

# case )
If we meet a right parentheses , right--.
    If right < 0, we need to add a left parentheses before it.
        Then we update right += 2 and res++
This part is easy and normal.

# case (
If we meet a left parentheses,
    we check if we have odd number ')' before.
        If we right, we have odd ')' before,
            but we want right parentheses in paires.
        So add one ')' here, then update right--; res++;.
Note that this part is not necessary if two consecutive right parenthesis not required.

Because we have ), we update right += 2.
'''

class Solution:
    def minInsertions(self, s):
        res = right = 0
        for c in s:
            if c == '(':
                if right % 2 == 1:
                    right -= 1
                    res += 1
                right += 2
            if c == ')':
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
        return right + res
