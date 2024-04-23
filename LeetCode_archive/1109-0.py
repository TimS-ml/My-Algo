'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i, j, k in bookings:
            ans[i - 1] += k
            ans[j] -= k
        for i in range(1, n):
            ans[i] += ans[i - 1]
        return ans[:-1]
