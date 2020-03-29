# https://leetcode-cn.com/problems/bold-words-in-string/
# httos://www.programiz.com/python-programming/methods/string/find
# [1] string searching
# [2] deal with overlap
# add start point and end point
# a mark string => what if mark overlap? like ab, cd in aabcdd case?
# s A s B e C e => s ABC e


class Solution:
    def boldWords(self, words, S: str) -> str:
        mark = [0] * len(S)
        for d in words:
            loc = S.find(d)
            # print(loc)
            mark[loc] = 1
        return mark            


# words, S
IN = [(["ab","bc"], "aabcd")]
useSet = 0
print(IN[useSet][0], IN[useSet][1])
print(Solution().boldWords(IN[useSet][0], IN[useSet][1]))

