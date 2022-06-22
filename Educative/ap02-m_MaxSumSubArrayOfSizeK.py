'''
https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP

# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)
'''

def max_sub_array_of_size_k(K, arr):
    ans = -float('inf')
    l, r = 0, 0
    s = 0

    # notice that we sum before increase index
    while r < len(arr):
        # right side
        s += arr[r]
        r += 1

        # print(f'window: {l}, {r}, sum: {s}')

        # left side
        # first window: [0 ~ K-1], at that time l=0, r=K
        # if r > K - 1:  # time to shrink l
        if r - l == K:  # time to shrink l
            if s > ans:
                ans = s
            s -= arr[l]
            l += 1

    return ans



def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
