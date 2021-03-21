# A brute-force algorithm will calculate the sum of every 5-element
# fix window + 1 pointer
# return average
def my(K, arr):
    ans = []
    # range is important
    # range = how many times the first element of sub arr can move
    # [xxxxx[_x_xxx]]
    #           K-1 (K=4)
    for i in range(len(arr) - K + 1):
        s = sum(arr[i:i + K])
        ans.append(s / K)
    return ans


def find_averages_of_subarrays(K, arr):
    result = []
    for i in range(len(arr) - K + 1):
        # find sum of next 'K' elements
        _sum = 0.0
        for j in range(i, i + K):
            _sum += arr[j]
        result.append(_sum / K)  # calculate average

    return result


def main():
    # result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    result = my(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
