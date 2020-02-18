# https://leetcode-cn.com/problems/pascals-triangle/
#    1 3 3 1 0 
# +  0 1 3 3 1
# =  1 4 6 4 1


class Solution(object):
    def generate(self, numRows):
        ans = [[1]]
        for i in range(1, numRows):
            ans += [list(map(lambda x, y: x+y, ans[-1]+[0], [0]+ans[-1]))]
        return ans[:numRows]


print(Solution().generate(5))
