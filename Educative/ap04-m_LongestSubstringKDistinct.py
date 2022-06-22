'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

'''

from collections import deque


def longest_substring_with_k_distinct(arr, K):
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
    print("Length of the longest substr1ing: " +
          str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substr1ing: " +
          str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substr1ing: " +
          str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
