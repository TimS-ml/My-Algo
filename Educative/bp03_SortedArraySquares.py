'''
sorted array
create a new array containing squares of all the numbers of the input array in the sorted order

# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)

# Pros and Cons and Notation:
Two ways:
[1] sort after calculate all the squares
[2] sort when calculate squares
- case: [-2, 0, 3], so we'd better move from left and right to middle
    - as long as left < right
    - appendright to achieve ascending order
'''

from heapq import heappush, heappop, heapify
from collections import deque

def make_squares_heap(arr):
    # the simplest way is to return sorted(ans)
    ans = [i**2 for i in arr]
    def heapsort(iterable):
        h = []
        for value in iterable:
            heappush(h, value)
        return [heappop(h) for i in range(len(h))]
    return heapsort(ans)

def make_squares(arr):
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


def main():
    print(make_squares([-2, -1, 0, 2, 3]))
    print(make_squares([-3, -1, 0, 1, 2]))
    print(make_squares([1, 2, 3, 4, 5]))


main()
