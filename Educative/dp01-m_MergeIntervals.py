'''
Given a list of intervals,
merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

# Code Explain:
- Time complexity: O(N * logN)
include sort
- Space complexity: O(N)

two pointers, maintain sliding window

'''


from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    intervals.sort(key=lambda x: x.start)

    ans = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        # overlap
        if intervals[i].start <= end:
            end = max(intervals[i].end, end)
        # no overlap, add [start, end] to ans
        else:
            ans.append(Interval(start, end))
            start = intervals[i].start
            end = intervals[i].end

    # the last one
    ans.append(Interval(start, end))
    return ans


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
