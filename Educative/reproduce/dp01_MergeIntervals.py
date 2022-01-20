'''
Given a list of intervals, 
merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

# Code Explain:
- Time complexity: O(N * logN)
include sort
- Space complexity: O(N)

# Pros and Cons and Notation:

Sort the intervals on the start time to ensure a.start <= b.start
If `a` overlaps `b` (i.e. b.start <= a.end), 
we need to merge them into a new interval `c` such that:
    c.start = a.start
    c.end = max(a.end, b.end)
We will keep repeating the above two steps to merge `c` 
with the next interval if it overlaps with `c`.

- input is unsorted start
  - do I need to sort by interval.start?
- case: 2+ intervals overlaps
  - [1, 3], [4, 5], [2, 7]
  - [1, 3], [4, 8], [1, 7]

- create 2 variables: start and end
  - if merge, update start and end
  - if no overlaps ???
    - that's why you need to sort interval.start (to make sure prev.start <= curr.start)
      - overlap:    [1, 3], [2, 7], [4, 8] => [1, 7], [4, 8]
      - no overlap: [1, 3], [4, 7], [4, 8] => [4, 7], [4, 8]
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
