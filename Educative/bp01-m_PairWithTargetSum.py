'''
# Code Explain:
Brute force
- Time complexity: O(n * log(n))

sorted nSum pattern
'''

# further (potential) improvement: skip or remove dupl
def pair_with_targetsum(arr, target_sum):
    l, r = 0, len(arr) - 1
    while l < r:
        s = arr[l] + arr[r]
        if s == target_sum:
            return [l, r]
        elif s < target_sum:  # make s bigger
            l += 1
        elif s > target_sum:  # make s smaller
            r -= 1
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    # print(pair_with_targetsum([1, 1, 1, 1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
