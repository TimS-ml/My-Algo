'''
sorted array
create a new array containing squares of all the numbers of the input array in the sorted order

# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)

check ap01, target_sum==0 case
sorted nSum pattern
'''

def make_squares(arr):
    l, r = 0, len(arr) - 1
    ans = []
    while l < r:
        if abs(arr[l]) < abs(arr[r]):
            ans.append(arr[r] ** 2)
            r -= 1
        else:
            ans.append(arr[l] ** 2)
            l += 1
    return ans[::-1]  # reverse is O(n), so doesn't matter


def main():
    print(make_squares([-2, -1, 0, 2, 3]))
    print(make_squares([-3, -1, 0, 1, 2]))
    print(make_squares([1, 2, 3, 4, 5]))


main()
