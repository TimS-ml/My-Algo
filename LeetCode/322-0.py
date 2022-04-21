'''
'''

class Solution:
    def xxx(self, coins, amount):
        cache = {}

        ans = float('INF')

        # number of moves
        def helper(num, remain):
            if remain == 0:
                ans = min(ans, num)
                return num

            elif remain in cache:
                return cache[remain]

            for c in coins:
                if remain - c >= 0:
                    helper(num + 1, remain - c)

        helper(0, amount)
        if ans == float('INF'):
            return -1
        return ans 
