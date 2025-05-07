from typing import List, Callable

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        # left to right
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                # candies[i] = max(candies[i], candies[i-1] + 1)
                candies[i] = candies[i-1] + 1
        
        # right to left
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)


current_solution: Callable[[List[int]], int] = None

def run_tests(input_file: str):
    global current_solution
    sol = Solution()
    
    # Change this to the function you want to test
    current_solution = sol.candy

    try:
        with open(input_file, 'r') as file:
            test_case = 1
            while True:
                # Read first line for ratings array
                line1 = file.readline().strip()
                
                # Check if we've reached end of file
                if not line1:
                    break
                    
                ratings = list(map(int, line1.split()))
                
                # Read second line for expected answer
                line2 = file.readline().strip()
                expected = int(line2)
                
                # Run the solution
                result = current_solution(ratings)
                
                # Print results
                print(f"Test Case {test_case}: {result}, {'Correct' if result == expected else 'Wrong'}")
                
                test_case += 1

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_tests("135.txt")
