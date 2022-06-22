'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

lc 003
'''

from collections import deque

def non_repeat_substring_brute(arr):
    l, r = 0, 0
    subarr = deque([])
    ans = 0
    valid = lambda x: len(x) == len(set(x))

    while r < len(arr):
        subarr.append(arr[r])
        r += 1

        if valid(subarr):
            ans = max(ans, len(subarr))
        else:
            subarr.popleft()

    return ans


# from labuladong
def non_repeat_substring_brute_v2(arr):
    # freq dict, make sure everything in char val=1
    # replace subarr
    window = {}  
    l, r = 0, 0
    ans = 0

    while r < len(arr):
        c = arr[r]
        r += 1

        window[c] = window.get(c, 0) + 1
        while window[c] > 1:
            d = arr[l]
            l += 1
            window[d] -= 1

        ans = max(ans, r - l)
    return ans


def non_repeat_substring(arr):
    rIdx = {}
    l, r = 0, 0
    ans = 0
    valid = lambda x: x not in rIdx

    while r < len(arr):
        if not valid(arr[r]):
            # print(rIdx, arr[r], l, r)
            l = rIdx[arr[l]] + 1
            l = max(r, l)  # this should be max...

        ans = max(ans, r - l + 1)
        rIdx[arr[r]] = r
        r += 1

    return ans


def main():
    print("Length of the longest substring: " +
          str(non_repeat_substring_brute("aabccbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring_brute("abbbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring_brute("abccde")))

    print("Length of the longest substring: " +
          str(non_repeat_substring_brute_v2("aabccbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring_brute_v2("abbbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring_brute_v2("abccde")))

    print("Length of the longest substring: " +
          str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abccde")))


main()
