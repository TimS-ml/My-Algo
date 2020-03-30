# https://leetcode-cn.com/problems/bold-words-in-string/
# https://zxi.mytechroad.com/blog/string/leetcode-758-bold-words-in-string/
# httos://www.programiz.com/python-programming/methods/string/find
# [1] string searching
# [2] deal with overlap
# add start point and end point or mark bold part to 1
# if point: [ A [ B ] C ] => [ ABC ], check leetcode 20
# this is not a clever approach, just for fun

class Solution:
    def boldWords(self, words, S: str) -> str:
        mark = [0] * len(S)
        for d in words:
            loc = S.find(d)
            # print(loc)
            if loc != -1:
                mark[loc] += 1
                mark[loc + len(d)] += 100
        return mark 


# words, S
IN = [(["ab","bc"], "aabcd"), ([], "aabcd"), (["ab","c"], "aabcd")]
useSet = 2
print(IN[useSet][0], IN[useSet][1])
print(Solution().boldWords(IN[useSet][0], IN[useSet][1]))

