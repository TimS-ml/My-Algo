'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''
from __future__ import print_function


class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def find_employee_free_time(schedule):
    result = []
    # TODO: Write your code here
    return result


def main():

    input = [[Interval(1, 3), Interval(5, 6)],
             [Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)],
             [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [Interval(2, 4)],
             [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
