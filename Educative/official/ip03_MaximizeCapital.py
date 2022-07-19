'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

lc 502

in each step:
- find [capital, profit] pair that:
  - captial <= current captical
  - maximum profit

current captial is a non-decrease seq
what if non-increasing?
- sort captial asc
- binary search find available idx, pool = list[:idx]

so, two steps:
- maintain a available capital pool after update
- pick maximum profit from pool
  - if no heap: sort numberOfProjects times
'''

from heapq import *


# one heap is good enough
def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    minCapitalHeap = []
    maxProfitHeap = []

    # insert all project capitals to a min-heap
    for i in range(0, len(profits)):
        heappush(minCapitalHeap, (capital[i], i))

    # let's try to find a total of 'numberOfProjects' best projects
    availableCapital = initialCapital
    for _ in range(numberOfProjects):
        # !!! find all projects that can be selected within the available capital and insert them in a max-heap
        while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
            capital, i = heappop(minCapitalHeap)
            heappush(maxProfitHeap, (-profits[i], i))

        # terminate if we are not able to find any project that can be completed within the available capital
        if not maxProfitHeap:
            break

        # select the project with the maximum profit
        availableCapital += -heappop(maxProfitHeap)[0]

    return availableCapital


def main():

    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
