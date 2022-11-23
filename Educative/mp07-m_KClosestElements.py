'''
# Code Explain:
- Time complexity: O(NlogN + klogk)
    NlogN is not the best solution
- Space complexity: O(N)

lc 658
'''


def find_closest_elements(arr, k, x):
    # Sort using custom comparator
    sorted_arr = sorted(arr, key = lambda num: abs(x - num))

    # Only take k elements
    result = []
    for i in range(k):
        result.append(sorted_arr[i])

    # Sort again to have output in ascending order
    return sorted(result)
