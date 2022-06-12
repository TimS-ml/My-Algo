'''
https://www.educative.io/courses/grokking-the-coding-interview/7D5NNZWQ8Wr

# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)
'''


# this is a more general approach for sliding window
def find_averages_of_subarrays(K, arr):
    ans = []
    l, r = 0, 0
    s = 0

    # notice that we sum before increase index
    while r < len(arr):
        # right side
        s += arr[r]
        r += 1

        print(f'window: {l}, {r}, sum: {s}')

        # left side
        # first window: [0 ~ K-1], at that time l=0, r=K
        # if r > K - 1:  # time to shrink l
        if r - l == K:  # time to shrink l
            ans.append(s/K)
            s -= arr[l]
            l += 1

    return ans


def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
