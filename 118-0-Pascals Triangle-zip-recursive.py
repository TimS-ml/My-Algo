# https://leetcode-cn.com/problems/pascals-triangle/


class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        def gen(nRows, out):
            if nRows == 1:
                return [1], [[1]]
            li1, _out = gen(nRows-1, out)
            li2 = [0] + li1[:-1]
            nlist = [a + b for a, b in zip(li1, li2)]
            nlist.append(1)
            _out.append(nlist)
            return nlist, _out
        temp, ans = gen(numRows, [])
        return ans


print(Solution().generate(5))

