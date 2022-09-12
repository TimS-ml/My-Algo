'''
# Code Explain:
sol 1: heap
- Time complexity:  O(logN + K*logK)
    We need O(logN) for Binary Search and O(KlogK) to insert the numbers in the Min Heap
- Space complexity: O(K)

sol 2: two pointers + binary search (better)
- Time complexity: O(logN + K)
    We need O(logN) for Binary Search and O(K) for finding the ‘K’ closest numbers using the two pointers
- Space complexity: O(1)

lc 658

sorted array, K closest number to X
'''

from heapq import *
from collections import deque


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if low > 0:
        return low - 1
    return low


def find_closest_elements(arr, K, X):
    index = binary_search(arr, X)
    low, high = index - K, index + K

    # 'low' should not be less than zero 
    low = max(low, 0)
    # 'high' should not be greater the size of the array
    high = min(high, len(arr) - 1)

    minHeap = []
    # add all candidate elements to the min heap, sorted by their absolute difference from 'X'
    for i in range(low, high + 1):
        heappush(minHeap, (abs(arr[i] - X), arr[i]))

    # we need the top 'K' elements having smallest difference from 'X'
    result = []
    for _ in range(K):
        result.append(heappop(minHeap)[1])

    result.sort()
    return result


def find_closest_elements_2(arr, K, X):
    result = deque()
    index = binary_search(arr, X)
    leftPointer, rightPointer = index, index + 1
    n = len(arr)
    for i in range(K):
        if leftPointer >= 0 and rightPointer < n:
            diff1 = abs(X - arr[leftPointer])
            diff2 = abs(X - arr[rightPointer])
            if diff1 <= diff2:
                result.appendleft(arr[leftPointer])
                leftPointer -= 1
            else:
                result.append(arr[rightPointer])
                rightPointer += 1
        elif leftPointer >= 0:
            result.appendleft(arr[leftPointer])
            leftPointer -= 1
        elif rightPointer < n:
            result.append(arr[rightPointer])
            rightPointer += 1

    return result



def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


def main_2():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements_2([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements_2([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements_2([2, 4, 5, 6, 9], 3, 10)))


main()
main_2()
