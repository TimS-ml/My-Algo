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


# Option A
def insert(intervals, new_interval):
    for i in range(len(intervals)):
        if intervals[i][0] > new_interval[0]:
            intervals.insert(i, new_interval)
            break

    # print(intervals)
    ans = []
    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        # start - interval - end - interval
        if end > intervals[i][0]:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
        else:
            ans.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]

    ans.append([start, end])
    return ans

            

def main():
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], 
                     [4, 6])))
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], 
                     [5, 6])))
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], 
                     [6, 7])))
    # print("Intervals after inserting the new interval: " +
    #       str(insert([[1, 3], [5, 7], [8, 12]],
    #                  [4, 10])))
    # print("Intervals after inserting the new interval: " +
    #       str(insert([[2, 3], [5, 7]],
    #                  [1, 4])))


main()
