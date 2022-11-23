'''
case = [1,1,1,2,2,3,3] k=2 => not happened

freq dict top k

O(n)
'''

class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        for n in nums:
            freq[str(n)] = freq.get(str(n), 0) + 1

        # [('-1', 2), ('2', 2), ('4', 1), ('1', 1), ('3', 1)]
        freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        return [val[0] for val in freq[:k]]


# nums = [1,1,1,2,2,3]
nums = [4,1,-1,2,-1,2,3]
k = 2
print(Solution().topKFrequent(nums, k))

