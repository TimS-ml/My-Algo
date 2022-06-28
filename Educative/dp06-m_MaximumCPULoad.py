'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''
from heapq import *


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load


def find_max_cpu_load(jobs):
    # TODO: Write your code here
    return -1


def main():
    print("Maximum CPU load at any time: " +
          str(find_max_cpu_load([job(
              1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
    print("Maximum CPU load at any time: " +
          str(find_max_cpu_load([job(6, 7, 10),
                                 job(2, 4, 11),
                                 job(8, 12, 15)])))
    print("Maximum CPU load at any time: " +
          str(find_max_cpu_load([job(
              1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()
