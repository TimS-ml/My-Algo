'''
Given two lists of intervals, find the intersection of these two lists.
Each list consists of disjoint intervals sorted on their start time.
The output list contains the common intervals between the two lists.

# Code Explain:
- Time complexity: O(N + M)
- Space complexity: O(1)

- len(a) might be different than len(b)
- can output intervals have intersection? No, since a and b does not have

- for element in b, find intersection in a, append to List

intervals pattern
'''


def merge(intervals_a, intervals_b):
    i, j = 0, 0
    ans = []
    while i < len(intervals_a) and j < len(intervals_b):
        a1, a2 = intervals_a[i][0], intervals_a[i][1]
        b1, b2 = intervals_b[j][0], intervals_b[j][1]

        # a1 <= b1 <= b2 <= a2
        # this not work a1 <= b1 and b2 <= a2
        if b2 >= a1 and a2 >= b1:
            ans.append([max(a1, b1), min(a2, b2)])

        if b2 < a2:
            j += 1
        else:
            i += 1
    return ans


def main():
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 6], [7, 9]],
                    [[2, 3], [5, 7]])))
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 7], [9, 12]],
                    [[5, 10]])))


main()
