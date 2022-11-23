'''
sorted array
create a new array containing squares of all the numbers of the input array in the sorted order

# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)

sorted
'''

from heapq import heappush, heappop
from collections import deque


# or you can use deque, then ans.appendleft
def make_squares(arr):
    # n = len(arr)
    # ans = [0 for _ in range(n)]
    # highestSquareIdx = n - 1
    # left, right = 0, n - 1  # this is a smart move, solving the <0 cases
    # while left <= right:
    #     leftSquare = arr[left] * arr[left]
    #     rightSquare = arr[right] * arr[right]
    #     if leftSquare > rightSquare:
    #         ans[highestSquareIdx] = leftSquare
    #         left += 1
    #     else:
    #         ans[highestSquareIdx] = rightSquare
    #         right -= 1
    #     highestSquareIdx -= 1

    # return ans
    l, r = 0, len(arr) - 1
    ans = deque()
    while l < r:
        l_sq, r_sq = arr[l] ** 2, arr[r] ** 2
        if l_sq > r_sq:
            ans.appendleft(l_sq)
            l += 1
        else:
            ans.appendleft(r_sq)
            r -= 1
    return ans


'''
Two ways:
[1] sort after calculate all the squares
[2] sort when calculate squares (official solution)
- case: [-2, 0, 3], so we'd better move from left and right to middle
    - as long as left < right
    - appendright to achieve ascending order

'''

# time complexity of nlogn, ignored `sorted` condition
def make_squares_heap(arr):
    # the simplest way is to return sorted(ans)
    ans = [i**2 for i in arr]
    def heapsort(iterable):
        h = []
        for value in iterable:
            heappush(h, value)
        return [heappop(h) for _ in range(len(h))]
    return heapsort(ans)


# time complexity of nlogn, ignored `sorted` condition
def make_squares_2(arr):
    arr = sorted(arr, key=lambda x: abs(x))
    return [x ** 2 for x in arr]


def main():
    print(make_squares([-2, -1, 0, 2, 3]))
    print(make_squares([-3, -1, 0, 1, 2]))
    print(make_squares([1, 2, 3, 4, 5]))


main()
