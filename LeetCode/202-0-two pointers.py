'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


class Solution:
    # brute, not recommend
    def isHappy(self, n: int) -> bool:
        if n <= 4 and n != 1:
            return False
        while True:
            n = sum([int(i)**2 for i in str(n)])
            if n == 4:
                return False
            if n == 1:
                return True

    # using hash set
    def isHappy_2(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum
    
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
    
        return n == 1

    def isHappy_3(self, n: int) -> bool:
        # this approach is slow
        # def get_next(n):
        #     return sum([int(i)**2 for i in str(n)])

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        slow = n
        fast = get_next(n)
        while slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return slow == 1


n = 19
print(Solution().isHappy(n))
