'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0 , len(s)-1
        while l <= r:
            if s[l]==s[r]:
                l += 1
                r -= 1
            else:
                sub1 = s[l:r]
                sub2 = s[l+1:r+1]
                print(sub1, sub2)
                return sub1 == sub1[::-1] or sub2 == sub2[::-1]

        return True

