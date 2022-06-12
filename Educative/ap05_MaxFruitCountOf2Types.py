'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

2 type of chars in unfix size window
'''

from collections import deque


def fruits_into_baskets(arr, K=2):
    ans = 0  # max length
    l, r = 0, 0
    subarr = deque([])
    
    while r < len(arr):
        if len(set(subarr)) < K:
            subarr.append(arr[r])
            r += 1
        elif len(set(subarr)) == K:
            ans = max(ans, len(subarr))
            subarr.append(arr[r])
            r += 1
        else:
            subarr.popleft()

    return ans


def main():
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
