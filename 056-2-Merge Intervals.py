# https://leetcode-cn.com/problems/merge-intervals/
# just another version


class Solution:
    def merge(self, intervals):
        ans = []
        for i in sorted(intervals):
            if ans and ans[-1][1] >= i[0]:
                ans[-1][1] = max(ans[-1][1], i[1])
            else:
                ans.append(i)
        return ans

intervals = [[1, 3], [2, 6], [15, 18], [8, 10]]
print(Solution().merge(intervals))
