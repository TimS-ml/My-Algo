'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

k = 2

preS[curr] = x

x - k, before curr

[1, 3) => (n0 + n1 + n2) - (n0)
sum(nums[i to j]) = preS[j+1] - preS[i] = k
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preS = [0]
        S = 0
        for i in range(len(nums)):
            S += nums[i]
            preS.append(S)
        
        dic = {0:1}
        ans = 0
        for j in range(len(nums)):
            t = preS[j+1] - k  # t before j+1, j+1 starts with 1
            if t in dic:
                ans += dic[t]
            dic[preS[j+1]] = dic.get(preS[j+1], 0) + 1
        
        return ans
            
    def subarraySum_old(self, nums: List[int], k: int) -> int:
        preS = [0]
        s = 0
        ans = 0
        
        # how many preS[i] - k = preS[j+1]
        # i to j+1
        #   1 1 1
        # 0 1 2 3
        freq = {}

        for i in range(len(nums)):
            s += nums[i]
            preS.append(s)
        
        print(preS)
        
        freq[0] = 1

        for i in range(1, len(nums)+1):
            # for j in range(0, i):
            #     if preS[i] - preS[j] == k:
            #         ans += 1
            target = preS[i] - k
            if target in freq:
                ans += freq[target]
            freq[preS[i]] = freq.get(preS[i], 0) + 1
            
        print(freq)
        return ans
