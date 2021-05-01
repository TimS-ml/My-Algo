'''
# Thought process:
logest common perfix depends on the shortest one

# Test Case:
'abcd', ''
'flower', 'flow'
'ccc', 'c', 'd'
["cir", "car"]
'''

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # special cases
        if len(strs) == 0:
            return ''
        
        # zip str
        zipped = list(zip(*strs))
        ans = ''

        # loop through zipped files
        for i in range(len(zipped)):
            # print(zipped[i])
            if len(set(zipped[i])) == 1:
                ans += zipped[i][0]
            # if != 1, means no common strs
            else:
                return ans
        return ans


strs = ["cir", "car"]
# strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
