'''
# Code Explain:
- Time complexity: O(NlogK)
- Space complexity: O(K)

lc 973
'''

from __future__ import print_function
from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # used for max-heap
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        # ignoring sqrt to calculate the distance
        return (self.x * self.x) + (self.y * self.y)

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
    maxHeap = []
    # put first 'k' points in the max heap
    for i in range(k):
        heappush(maxHeap, points[i])

    # go through the remaining points of the input array, if a point is closer to the origin than the top point
    # of the max-heap, remove the top point from heap and add the point from the input array
    for i in range(k, len(points)):
        if points[i].distance_from_origin() < maxHeap[0].distance_from_origin():
            heappop(maxHeap)
            heappush(maxHeap, points[i])

    # the heap has 'k' points closest to the origin
    return maxHeap


def main():

    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
