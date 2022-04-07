'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

# Example
(()))) => balanced
(())()))) = 
    (
        ()) ())
    )) => balanced


# Explanation
ans represents the number of left/right parentheses already added.
right represents the number of right parentheses needed.

# case (
If we meet a left parentheses,
    check if we have odd number ')' before.
        If we have odd ')' before,
            but we want right parentheses in paires.
            So add one ')' here, then update right--; ans++;.
    !!! Note that this part is not necessary if two consecutive right parenthesis not required.
        True: ())()), False: ()()))

Because we have ), we update right += 2.


# case )
If we meet a right parentheses , right--.
    If right < 0, we need to add a left parentheses before it.
        Then we update right += 2 and ans++
This part is easy and normal.
'''

class Solution:
    def minInsertions(self, s):
        ans = right = 0
        for c in s:
            if c == '(':
                # ()())) at 3rd '('
                # we need ) but got (
                #   add ) to balance string
                #   remove need of )
                # i.e. insert and turn ()( to ())(
                if right % 2 == 1:
                    right -= 1
                    ans += 1
                right += 2
            if c == ')':
                # )) at 1st ')'
                # append ( as ans += 1
                # append ) as right = 1
                # )) at 2nd ')'
                # right -= 1
                right -= 1
                if right < 0:
                    right += 2
                    ans += 1
        return right + ans
