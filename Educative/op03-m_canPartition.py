'''
# Code Explain:
- Time complexity: O(N * S)
- Space complexity: O(N * S)
The algorithm has the time and space complexity of O(N*S), where ‘N’ represents total numbers and ‘S’ is the total s of all the numbers.



Top down
'''


def can_partition(num, s):
    cache = [[-1 for _ in range(s + 1)] for _ in range(len(num))]

    def top_down_dp(cache, idx, curr_sum):
        if curr_sum == 0:
            return 1

        if idx >= len(num):
            return 0

        if cache[idx][curr_sum] == -1:
            if num[idx] <= curr_sum:
                # include curr idx
                if top_down_dp(cache, idx + 1, curr_sum - num[idx]):
                    cache[idx][curr_sum] = 1
                    return 1

            # not include curr idx
            cache[idx][curr_sum] = top_down_dp(cache, idx + 1, curr_sum)

        return cache[idx][curr_sum]
    
    if top_down_dp(cache, 0, s):
        return True
    else:
        return False


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
