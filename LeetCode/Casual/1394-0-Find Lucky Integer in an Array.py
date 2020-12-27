# https://leetcode-cn.com/problems/find-lucky-integer-in-an-array/

from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = {}
        for n in arr:
            dic[n] = dic.get(n, 0) + 1
        dic = {
            k: v
            for k, v in sorted(
                dic.items(), key=lambda item: item[1], reverse=True)
        }
        print(dic)
        for i in dic:
            if dic[i] == i:
                return i
        return -1


# arr = [2, 2, 3, 4]
arr = [1, 2, 2, 3, 3, 3]
print(Solution().findLucky(arr))
