'''
https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ

# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

'''

def smallest_subarray_with_given_sum(S, arr):
    ans = len(arr) + 1
    l, r = 0, 0
    s = 0

    while r < len(arr):
        s += arr[r]
        r += 1

        # a valid solution
        while s >= S:
            # careful with index difference
            # case: the 1st element is greater than S
            #       r=1, l=0, thus we should directly use r-l
            #       since at specific s = sum([x...y]), r=y+1, l=x
            ans = min(ans, r - l)
            s -= arr[l]
            l += 1

    return ans


def main():
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
