'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

'''

from typing import List, Callable


class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # convert edge case: add 0 to the head and tail
        flowerbed = [0] + flowerbed + [0]

        cnt = 0
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                cnt += 1

        return cnt >= n


current_solution: Callable[[List[int], int], bool] = None


def run_tests(input_file: str):
    global current_solution
    sol = Solution()

    # Change this to the function you want to test
    current_solution = sol.canPlaceFlowers

    try:
        with open(input_file, 'r') as file:
            test_case = 1
            while True:
                flowerbed = file.readline().strip()
                if not flowerbed:  # End of file
                    break
                flowerbed = list(map(int, flowerbed.split()))
                n = int(file.readline().strip())
                expected = bool(int(file.readline().strip()))

                result = current_solution(flowerbed, n)
                print(
                    f"Test Case {test_case}: {result}, {'Correct' if result == expected else 'Wrong'}"
                )

                test_case += 1

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_tests("605.txt")
