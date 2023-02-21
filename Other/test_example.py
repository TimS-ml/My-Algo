class Solution:
    def validPalindrome(self, s: str, t: str) -> bool:
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


testFunc = Solution().validPalindrome

S = [
    '',
    'a',        
    'aaa',
    'abobca',
    'abab', 
    'abc'
]

T = [
    '',
    'a',        
    'aaa',
    'abobca',
    'abab', 
    'abc'
]

for s, t in zip(S, T):
    print(s, t, testFunc(s, t))

