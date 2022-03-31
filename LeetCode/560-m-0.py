'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     preS = [0]
    #     s = 0
    #     ans = 0
    #     for i in range(len(nums)):
    #         s += nums[i]
    #         preS.append(s)
    #     
    #     # print(preS)
    #     for i in range(1, len(nums)+1):
    #         for j in range(0, i):
    #             # print(i, j)
    #             if preS[i] - preS[j] == k:
    #                 ans += 1

    #     # for i in range(0, len(nums)):
    #     #     for j in range(i, len(nums)+1):
    #     #         if preS[j] - preS[i] == k:  # j ahead i
    #     #             ans += 1
    #     return ans   #     return ans

    def subarraySum(self, nums: List[int], k: int) -> int:
        preS = []
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
        
        for i in range(len(nums)):
            target = preS[i] - k
            if target in freq:
                ans += freq[target]
            freq[target] = freq.get(target, 0) + 1
        
        return ans
