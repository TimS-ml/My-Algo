'''
# Code Explain:
sol 1
- Time complexity: O(NlogN)
- Space complexity: O(N)

sol 2
- Time complexity: O(NlogK2)
- Space complexity: O(K2)

'''
from heapq import *


def find_sum_of_elements(nums, k1, k2):
    minHeap = []
    # insert all numbers to the min heap
    for num in nums:
        heappush(minHeap, num)

    # remove k1 small numbers from the min heap
    for _ in range(k1):
        heappop(minHeap)

    elementSum = 0
    # sum next k2-k1-1 numbers
    for _ in range(k2 - k1 - 1):
        elementSum += heappop(minHeap)

    return elementSum


# max heap
def find_sum_of_elements_2(nums, k1, k2):
    maxHeap = []
    # keep smallest k2 numbers in the max heap
    # !!! this will keep the size smaller
    for i in range(len(nums)):
        if i < k2 - 1:
            heappush(maxHeap, -nums[i])
        elif nums[i] < -maxHeap[0]:
            heappop(maxHeap
                    )  # as we are interested only in the smallest k2 numbers
            heappush(maxHeap, -nums[i])

    # get the sum of numbers between k1 and k2 indices
    # these numbers will be at the top of the max heap
    elementSum = 0
    for _ in range(k2 - k1 - 1):
        elementSum += -heappop(maxHeap)

    return elementSum


def main():

    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
