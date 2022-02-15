'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)



ord('A')=65

AB  =  1*26 + 2
XY  = 24*26 + 25
ZZ  = 26*26
AAB = 1*26**2 + AB = 704
'''


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_li = list(columnTitle)[::-1]
        ans = 0
        for i in range(len(col_li)):
            dig = ord(col_li[i]) - ord('A') + 1
            ans += dig * 26**i
        return ans

    def titleToNumber_2(self, columnTitle: str) -> int:
        ans = 0
        # order of i is: 2, 1, 0
        power = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            dig = ord(columnTitle[i]) - ord('A') + 1
            ans += dig * power
            power *= 26
        return ans


columnTitle = 'AAB'
print(Solution().titleToNumber_2(columnTitle))
