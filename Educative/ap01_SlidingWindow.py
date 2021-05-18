'''
https://www.educative.io/courses/grokking-the-coding-interview/7D5NNZWQ8Wr

# Code Explain:
- Time complexity: O(N)
- Space complexity: O()

Time for arr[i:i + K] is O(K)

# Pros and Cons and Notation:
A brute-force algorithm will calculate the **sum of every 5-element**
fix window + 1 pointer
return average
'''


def find_averages_of_subarrays(K, arr):
    ans = []
    # range is important
    # range = how many times the first element of sub arr can move
    # [xxxxx[_x_xxx]]
    #           K-1 (K=4)
    for i in range(len(arr) - K + 1):
        # find sum of next 'K' elements
        s = sum(arr[i:i + K])
        ans.append(s / K)  # calc average

    return ans


def main():
    # result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
