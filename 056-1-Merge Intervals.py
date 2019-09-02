# https://leetcode-cn.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals):
        # 先把intervals按照第一个值进行排序
        intervals.sort()
        # print(intervals)
        n = len(intervals)
        if n == 0:
            return []

        result = [intervals[0]]
        for i in range(1, n):
            # 有重合，则重合区间的右值为最大的那个
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        return result


intervals = [[1, 3], [2, 6], [15, 18], [8, 10]]
print(Solution().merge(intervals))
