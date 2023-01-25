'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        ans = -1
        for num in nums:
            s = sum([int(digit) for digit in str(num)])
            if s not in dic:
                dic[s] = num
            else:
                ans = max(ans, dic[s] + num)
                dic[s] = max(dic[s], num)
        return ans

    # a correct way to maintain the sorted candidates
    def maximumSum_2(self, nums: List[int]) -> int:
        d, mx = defaultdict(list), -1
        digits = lambda x: sum(map(int, list(str(x))))      # <-- sum-of-digits function
       
        for n in nums:                                      # <-- construct max-heaps
            heappush(d[digits(n)],-n)                       #     (note "-n") 

        for i in d:                                         # <-- pop the two greatest values off
            if len(d[i]) > 1:                               #     each maxheap (when possible) and
                mx= max(mx, -heappop(d[i])-heappop(d[i]))   #     compare with current max value.
                                                           
        return mx
