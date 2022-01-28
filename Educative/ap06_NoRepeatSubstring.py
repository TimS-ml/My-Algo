'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

# Pros and Cons and Notation:
'''

'''
- change freq dict in ap04 to index dict
    - len(dic) should <= 2
    - else, the 3rd char is arr[end]
        - before updating arr end index to dic, update start to dic[arr[end]] + 1 or unchange
        - update / not update start: the new start should be >= than old start
- the order of each steps?
    - we only need to update the edge of dynamic window
'''
def non_repeat_substring(arr):
    ans = 0
    start = 0
    dic = {}
    for end in range(len(arr)):
        rchar = arr[end]
        if rchar in dic:
            start = max(start, dic[rchar] + 1)
        dic[rchar] = end
        ans = max(ans, end - start + 1)
    return ans


def main():
    print("Length of the longest substring: " +
          str(non_repeat_substring("aabccbb")))
    # print("Length of the longest substring: " +
    #       str(non_repeat_substring_v2("aabccbb")))
    # print("Length of the longest substring: " +
    #       str(non_repeat_substring("abbbb")))
    # print("Length of the longest substring: " +
    #       str(non_repeat_substring("abccde")))


main()
