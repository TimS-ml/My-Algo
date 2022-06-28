'''
Given an array of intervals representing ‘N’ appointments, 
find out if a person can attend all the appointments.

# Code Explain:
- Time complexity: O(N * logN)
- Space complexity: O(N)

'''


def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        # not <= !
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


def main():
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()
