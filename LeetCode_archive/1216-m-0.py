'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Feedback:
- Check edge cases!!!
    forgot l==r-1 => l+1, r-1 will out of boundary!!!

'''

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def helper(l, r, op):
            nonlocal cache

            if (l, r, op) in cache:
                return cache[(l, r, op)]

            if l == r:
                return True
            elif l == r-1:
                if s[l] == s[r]:
                    return True
                elif op <= k-1:
                    return True
                else:
                    return False

            if op > k:
                return False

            # do sth
            if s[l] == s[r]:
                ans = helper(l + 1, r - 1, op)
            else:
                ans = helper(l + 1, r, op+1) or helper(l, r - 1, op+1)

            cache[(l, r, op)] = ans
            return ans

        cache = {}

        return helper(0, len(s)-1, 0)
