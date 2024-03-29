'''
# Code Explain:
Brute force
- Time complexity: O(n * log(n))

sol1:
- Time complexity: O(n)
- Space complexity: O(1)
sorted, 2 pointers from left and right move to middle

sol2:
- Time complexity: O(n)
- Space complexity: O(n)
this is more flexible approach, the array no need to be sorted
'''

def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr) - 1
    while (left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]

        if target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum
    return [-1, -1]


def pair_with_targetsum_2(arr, target_sum):
    dic = {}  # to store numbers and their indices
    for i, num in enumerate(arr):
        if target_sum - num in dic:
            return [dic[target_sum - num], i]
        else:
            dic[arr[i]] = i
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
