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
        # if len(prices) <= 1: return 0
        ans = 0
        for i in range(1, len(prices)):
            # if (gap := prices[i] - prices[i-1]) > 0: ans += gap
            gap = prices[i] - prices[i-1]
            if gap > 0: ans += gap
        return ans


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
