from typing import List, Callable


class Solution:

    def candy(self, ratings: List[int]) -> int:
        candies = [1 for _ in range(len(ratings))]

        # left to right
        idx = 1
        while idx < len(ratings):
            if ratings[idx - 1] < ratings[idx]:
                if candies[idx - 1] >= candies[idx]:
                    candies[idx] = candies[idx - 1] + 1
            idx += 1

        # right to left
        idx = len(ratings) - 2
        while idx >= 0:
            if ratings[idx] > ratings[idx + 1]:
                if candies[idx] <= candies[idx + 1]:
                    candies[idx] = candies[idx + 1] + 1
            idx -= 1

        # print(candies)
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
                print(
                    f"Test Case {test_case}: {result}, {'Correct' if result == expected else 'Wrong'}"
                )

                test_case += 1

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_tests("135.txt")
