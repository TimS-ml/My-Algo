'''
sorted array
create a new array containing squares of all the numbers of the input array in the sorted order

# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)

# Pros and Cons and Notation:
sorted, 2 pointers start at middle (0) and move to the two ends
make comparison to decide which pointer to move
'''

def make_squares(arr):
    n = len(arr)
    ans = [0 for _ in range(n)]
    highestSquareIdx = n - 1
    left, right = 0, n - 1  # this is a smart move, solving the <0 cases
    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        if leftSquare > rightSquare:
            ans[highestSquareIdx] = leftSquare
            left += 1
        else:
            ans[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1

    return ans


def main():
    print(make_squares([-2, -1, 0, 2, 3]))
    print(make_squares([-3, -1, 0, 1, 2]))
    print(make_squares([1, 2, 3, 4, 5]))


main()
