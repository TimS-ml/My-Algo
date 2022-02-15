'''
Given a list of intervals, 
merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

# Code Explain:
- Time complexity: O(N * logN)
include sort
- Space complexity: O(N)



Sort the intervals on the start time to ensure a.start <= b.start
If `a` overlaps `b` (i.e. b.start <= a.end), 
we need to merge them into a new interval `c` such that:
    c.start = a.start
    c.end = max(a.end, b.end)
We will keep repeating the above two steps to merge `c` 
with the next interval if it overlaps with `c`.
'''


from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    if len(intervals) < 2:
        return intervals

    # sort the intervals on the start time
    intervals.sort(key=lambda x: x.start)

    mergedIntervals = []
    start = intervals[0].start
    end = intervals[0].end

    # start with 1st element
    for i in range(1, len(intervals)):
        interv = intervals[i]
        # overlapping intervals, adjust the 'end'
        if interv.start <= end:
            end = max(interv.end, end)
        # non-overlapping interval, add the previous internval and reset
        else:
            mergedIntervals.append(Interval(start, end))
            # !!! update comparison standard
            start = interv.start
            end = interv.end

    # add the last interval
    mergedIntervals.append(Interval(start, end))
    return mergedIntervals


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
