'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from heapq import *


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    projects = [[capital[i], profits[i]] for i in range(len(capital))]
    projects.sort(key = lambda x: -x[0])

    maxProfitHeap = []

    for _ in range(numberOfProjects):
        while projects and projects[-1][0] <= initialCapital:
            heappush(maxProfitHeap, -projects.pop()[1])
        if maxProfitHeap:
            initialCapital -= heappop(maxProfitHeap)
        else:
            break

    return initialCapital


def main():

    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
