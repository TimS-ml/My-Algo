'''
# Code Explain:
- Time complexity: O(2^N)
- Space complexity: O(N)



Basic Solution
for each number 'i' 
  add number 'i' to S1 and recursively process the remaining numbers
  add number 'i' to S2 and recursively process the remaining numbers
return the minimum absolute difference of the above two sets
'''


def can_partition(num):
    return can_partition_recursive(num, 0, 0, 0)


def can_partition_recursive(num, currentIndex, sum1, sum2):
    # base check
    if currentIndex == len(num):
        return abs(sum1 - sum2)

    # recursive call after including the number at the currentIndex in the first set
    diff1 = can_partition_recursive(num, currentIndex + 1,
                                    sum1 + num[currentIndex], sum2)

    # recursive call after including the number at the currentIndex in the second set
    diff2 = can_partition_recursive(num, currentIndex + 1, sum1,
                                    sum2 + num[currentIndex])

    return min(diff1, diff2)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()

