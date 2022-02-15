'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()


ord('a') - ord('A') = 32! not 26

s could be: '"Hello@[]"'
'''


class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if 'A' <= s[i] <= 'Z':
                s[i] = chr(ord(s[i]) + 32)
        return ''.join(s)

    # for A-Z and a-z only
    def toLowerCase_2(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            s[i] = chr(ord(s[i]) | 32)
        return ''.join(s)


print(Solution().toLowerCase_2('Hiiii'))
