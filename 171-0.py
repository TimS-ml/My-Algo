class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_li = list(columnTitle)[::-1]
        ans = 0
        for i in range(len(col_li)):
            dig = ord(col_li[i]) - ord('A') + 1
            ans += dig * 26**i
        return ans

