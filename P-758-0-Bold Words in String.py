# https://leetcode-cn.com/problems/bold-words-in-string/
# [1] string searching
# [2] deal with overlap: 
# add start point and end point
# s A s B e C e => s ABC e


class Solution:
    def boldWords(self, words, S: str) -> str:
        for i in range(S):

# words, S
IN = [(["ab","bc"], "aabcd")]
useSet = 0
print(IN[useSet][0], IN[useSet][1])
print(Solution().boldWords(IN[useSet][0], IN[useSet][1]))

