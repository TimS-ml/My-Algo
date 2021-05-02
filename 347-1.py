from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1  # init

        dic_value_sort = {}
        for key, val in sorted(dic.items(), key=lambda item: item[1],
                           reverse=True):
            dic_value_sort[key] = val

        ans = list(dic_value_sort.keys())
        if len(ans) != k:
            ans = ans[:k]
        
        return ans

nums = [1, 1, 1, 2, 2, 3]
k = 2
# nums = [-1, -1]
# k = 1
print(Solution().topKFrequent(nums, k))
