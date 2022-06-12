'''
https://www.educative.io/courses/grokking-the-coding-interview/7D5NNZWQ8Wr

# Code Explain:
- Time complexity: O(N)
- Space complexity: O()

Time for arr[i:i + K] is O(K)


A brute-force algorithm will calculate the **sum of every 5-element**
fix window + 1 pointer
return average
'''


def find_averages_of_subarrays_brute(K, arr):
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


# optimized
# 2 pointers with fixed gap

# for the fixed gap
def my(K, arr):
    ans = []
    # 0 to (len(arr)-K+1)
    start = 0
    s = sum(arr[:K - 1])  # sum of first K-1 numbers
    for end in range(K - 1, len(arr)):
        s += arr[end]
        ans.append(s / K)
        s -= arr[start]
        start += 1
    return ans


# for un-fixed gap, more general approach
def my2(K, arr):
    ans = []
    start = 0
    s = 0
    for end in range(len(arr)):
        s += arr[end]
        if end >= K - 1:  # start at [0 ~ K-1]
            ans.append(s / K)
            s -= arr[start]
            start += 1
    return ans


def find_averages_of_subarrays(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= K - 1:
            result.append(windowSum / K)  # calculate the average
            windowSum -= arr[windowStart]  # subtract the element going out
            windowStart += 1  # slide the window ahead
    return result


def main():
    result = my(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    # result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    # result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    # result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
