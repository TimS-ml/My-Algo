'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

case 1: [1, 3, 2, 4, 5]
case 2: [3, 2, 6, 5]
'''

from typing import List, Callable


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            # if (gap := prices[i] - prices[i-1]) > 0: ans += gap
            gap = prices[i] - prices[i-1]
            if gap > 0: ans += gap
        return ans

    # NOTE: This recursive approach does work because the problem has optimal substructure
    # i.e. the optimal solution can be constructed from optimal solutions of its subproblems. 
    # However, it has exponential time complexity O(n²) without memoization, 
    # making it much less efficient than the greedy approach.
    def maxProfit_2(self, prices: List[int]) -> int:
        return Solution().calculate(prices, 0)
    
    def calculate(self, prices: List[int], start: int = 0) -> int:
        if start >= len(prices): return 0
        max_profit = 0
        for idx in range(start, len(prices)):
            curr_profit = 0
            for idx2 in range(idx + 1, len(prices)):
                if prices[idx] < prices[idx2]:
                # Calculate profit = (profit from current transaction) + (max profit from remaining days)
                profit = self.calculate(prices, idx2 + 1) + prices[idx2] - prices[idx]
                curr_profit = max(profit, curr_profit)
            max_profit = max(curr_profit, max_profit)
        return max_profit

        
    # You could also solve this with DP by maintaining two states:
    # hold[i]: maximum profit on day i if we're holding a stock
    # notHold[i]: maximum profit on day i if we're not holding a stock
    def maxProfit_3(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        
        # Initialize DP arrays
        hold = [0] * n
        notHold = [0] * n
        
        # Base cases
        hold[0] = -prices[0]  # Buy the stock on day 0
        notHold[0] = 0        # Don't buy anything on day 0
        
        for i in range(1, n):
            # If holding stock on day i, either we were holding on day i-1, 
            # or we bought on day i
            hold[i] = max(hold[i-1], notHold[i-1] - prices[i])
            
            # If not holding stock on day i, either we weren't holding on day i-1, 
            # or we sold on day i
            notHold[i] = max(notHold[i-1], hold[i-1] + prices[i])
        
        # Final answer is maximum profit without holding stock on the last day
        return notHold[n-1]

current_solution: Callable[[List[int]], int] = None

def run_tests(input_file: str):
    global current_solution
    sol = Solution()
    
    # Change this to the function you want to test
    current_solution = sol.maxProfit

    try:
        with open(input_file, 'r') as file:
            test_case = 1
            while True:
                # Read the number of prices
                n = int(file.readline().strip())
                if n == 0:  # End of file
                    break
                
                # Read the prices array
                prices = list(map(int, file.readline().strip().split()))
                
                # Read the expected answer
                expected = int(file.readline().strip())
                
                result = current_solution(prices)
                print(f"Test Case {test_case}: {result}, {'Correct' if result == expected else 'Wrong'}")
                
                test_case += 1

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_tests("122.txt")
