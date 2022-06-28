'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''
import heapq


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def min_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x.start)
    heap = []  # stores the end time of meetings
    for meet in meetings:
        if heap and meet.start >= heap[0]:
            # means two meetings can use the same room
            heapq.heapreplace(heap, meet.end)  # pop + push
        else:
            # a new room is allocated
            heapq.heappush(heap, meet.end)
    return len(heap)


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
