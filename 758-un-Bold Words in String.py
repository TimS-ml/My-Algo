# https://leetcode-cn.com/problems/bold-words-in-string/
# https://zxi.mytechroad.com/blog/string/leetcode-758-bold-words-in-string/
# https://www.programiz.com/python-programming/methods/string/find
# [1] string searching
# [2] deal with overlap
# add start point and end point or mark bold part to 1
# this is not a clever approach, just for fun, check leetcode 20
# if point: [ A [ B ] C ] => [ ABC ]
# if point: [ A [[ B ] C ]] => [ ABC ]
# if point: [ A ][ B  C ] => [ ABC ]


class Solution:
    def boldWords(self, words, S: str) -> str:
        mark = {'start': [], 'end': []}
        for d in words:
            loc = S.find(d)
            # print(loc)
            if loc != -1:
                mark['start'].append(loc)
                mark['end'].append(loc + len(d))

        stack = 0
        for i in range(len(S)):
            if i in mark['start']:
                stack += 1
            elif i in mark['end']:
                stack -= 1
                if stack == 0:
                    print('end:', i)


# words, S
IN = [(["ab", "bc"], "aabcd"), ([], "aabcd"), (["ab", "c"], "aabcd")]
useSet = 2
print(IN[useSet][0], IN[useSet][1])
print(Solution().boldWords(IN[useSet][0], IN[useSet][1]))
