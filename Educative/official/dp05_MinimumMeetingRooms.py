'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

lc 253

Similar Problems
Problem 1: 
Given a list of intervals, find the point where the maximum number of intervals overlap

Problem 2: 
Given a list of intervals representing the arrival and departure times of trains to a train station, 
our goal is to find the minimum number of platforms required for the train station so that no train has to wait

'''
from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end


def min_meeting_rooms(meetings):
    # sort the meetings by start time
    meetings.sort(key=lambda x: x.start)

    minRooms = 0
    minHeap = []
    for meeting in meetings:
        # remove all the meetings that have ended
        while (len(minHeap) > 0 and meeting.start >= minHeap[0].end):
            heappop(minHeap)
        # add the current meeting into min_heap
        heappush(minHeap, meeting)
        # all active meetings are in the min_heap, so we need rooms for all of them.
        minRooms = max(minRooms, len(minHeap))
    return minRooms


def main():
    print("Minimum meeting rooms required: " + str(
        min_meeting_rooms(
            [Meeting(4, 5),
             Meeting(2, 3),
             Meeting(2, 4),
             Meeting(3, 5)])))
    print(
        "Minimum meeting rooms required: " +
        str(min_meeting_rooms(
            [Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print(
        "Minimum meeting rooms required: " +
        str(min_meeting_rooms(
            [Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print(
        "Minimum meeting rooms required: " +
        str(min_meeting_rooms(
            [Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " + str(
        min_meeting_rooms(
            [Meeting(4, 5),
             Meeting(2, 3),
             Meeting(2, 4),
             Meeting(3, 5)])))


main()
