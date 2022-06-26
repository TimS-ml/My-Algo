'''
Given a list of non-overlapping intervals sorted by their start time, 
insert a given interval at the correct position and 
merge all necessary intervals to produce a list that has only mutually exclusive intervals.

# Code Explain:
- Time complexity: O(N)  # no sort
- Space complexity: O(N)

[1] intervals already no overlap + sorted by start time => try not use sort
Two options:
[a] Loop through all intervals then insert new_interval into correct position
    then use same code as dp01
[b] Skip the non-overlapping intervals (interval.end < new_interval.start), then merge interval


follow up:
Not sorted by start time?
    print("Intervals after inserting the new interval: " +
          str(insert([[5, 7], [1, 3], [8, 12]], 
                     [4, 6])))
'''


def insert(intervals, new_interval):


def main():
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], 
                     [4, 6])))
    # print("Intervals after inserting the new interval: " +
    #       str(insert([[1, 3], [5, 7], [8, 12]],
    #                  [4, 10])))
    # print("Intervals after inserting the new interval: " +
    #       str(insert([[2, 3], [5, 7]],
    #                  [1, 4])))


main()
