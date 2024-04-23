'''
# Code Explain:
sol 1
- Time complexity: O(N logK)
- Space complexity: O(N)

sol 2
- Time complexity: O(N)
- Space complexity: O(N)

sol 3
- Time complexity: O(N)
- Space complexity: O(N)

# sol 1
if you put entire list to heap, the time complexity is O(N logN) then it's meaningless

# sol 2
b search's search space: distance
- range: between low_dist and high_dist = 0, max(dist_list)

func of mid_dist low or high: compare 'len(close) based on curr mid_dist' with k

tricky part: we search distance (an increasing sequence that can be searched)
- check 1011
'''

import heapq
import random
from typing import List

class Solution:
    # heap
    # Since heap is sorted in increasing order,
    # use negate the distance to simulate max heap
    # and fill the heap with the first k elements of points
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def sqDist(point):
            return point[0] ** 2 + point[1] ** 2

        # heap contains 0-k-1
        # build heap, (dist, idx) pair, first k elements !!!
        heap = [(-sqDist(points[i]), i) for i in range(k)]
        heapq.heapify(heap)

        # loop k~len(points)
        # maintain heap of size k
        for i in range(k, len(points)):
            dist = -sqDist(points[i])
            # - curr dist > - top node dist <=> top node dist > curr dist
            if dist > heap[0][0]:
                # If this point is close_idx than the kth farthest,
                # discard the farthest point and add this one
                heapq.heappushpop(heap, (dist, i))

        return [points[i] for (_, i) in heap]

    # binary select !!! O(N) time and space
    def kClosest_2(self, points: List[List[int]], k: int) -> List[List[int]]:
        def sqDist(point):
            return point[0] ** 2 + point[1] ** 2

        def splitDist(remain_idx, dist_list, mid_dist):
            """Split the dist_list around the midpoint
            and return them in separate lists."""
            close_idx, far_idx = [], []
            for index in remain_idx:
                if dist_list[index] <= mid_dist:
                    close_idx.append(index)
                else:
                    far_idx.append(index)
            return close_idx, far_idx

        # list of dist
        dist_list = [sqDist(point) for point in points]

        # list of idx
        remain_idx = [i for i in range(len(points))]

        # Define the initial binary search range
        low_dist, high_dist = 0, max(dist_list)

        # Perform a binary search of the dist_list
        # to find the k closest points
        closest = []
        while k:
            mid_dist = (low_dist + high_dist) / 2
            close_idx, far_idx = splitDist(remain_idx, dist_list, mid_dist)
            if len(close_idx) > k:
                # If more than k points are in the close_idx dist_list
                # then discard the far_idx points and continue
                remain_idx = close_idx
                high_dist = mid_dist
            else:
                # Add the close_idx points to the answer array and keep
                # searching the far_idx dist_list for the remain_idx points
                k -= len(close_idx)
                closest.extend(close_idx)
                remain_idx = far_idx
                low_dist = mid_dist

        # Return the k closest points using the reference indices
        return [points[i] for i in closest]


    # quickselect
    def kClosest_3(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]
