'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def helper(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return -1
            if remain in cache:
                return cache[remain]
            
            ans = float('inf')

            for c in coins:
                subprob = helper(remain - c)
                if subprob == -1:
                    continue
                # start with {remain=0: 0}
                # each helper stack will +1 for subprob
                ans = min(ans, subprob + 1)
            
            if ans != float('inf'):
                cache[remain] = ans
            else:
                cache[remain] = -1
            return cache[remain]
        
        return helper(amount)
