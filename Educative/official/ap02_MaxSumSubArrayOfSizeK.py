'''
https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP

# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)


two pointers: start, end
'''


# 2 pointers with fixed gap
def my(K, arr):
    ans = []
    # 0 to (len(arr)-K+1)
    start = 0
    s = sum(arr[:K - 1])  # sum of first K-1 numbers
    for end in range(K - 1, len(arr)):
        s += arr[end]
        ans.append(s)
        s -= arr[start]
        start += 1
    return max(ans)


# O(N*K), where 'N' is the total number of elements in the given array
def brute_max_sub_array_of_size_k(k, arr):
    max_sum, window_sum = 0, 0

    for i in range(len(arr) - k + 1):
        window_sum = sum(arr[i:i + k])
        #  window_sum = 0
        #  for j in range(i, i + k):
        #      window_sum += arr[j]
        max_sum = max(max_sum, window_sum)
        return max_sum


# O(N), where 'N' is the total number of elements in the given array
def max_sub_array_of_size_k(k, arr):
    max_sum, window_sum = 0, 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead
    return max_sum


def main():
    print("Maximum sum of a subarray of size K: " +
          str(my(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(my(2, [2, 3, 4, 1, 5])))
    # print("Maximum sum of a subarray of size K: " +
    #       str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    # print("Maximum sum of a subarray of size K: " +
    #       str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
