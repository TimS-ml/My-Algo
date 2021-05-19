'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

# Pros and Cons and Notation:
same as ap04
but ap04, ap05 dic is frequency dict
if dic[left_fruit] == 0:
    del dic[left_fruit]
use len(dic) to check how many chars  

in ap06, dic is index dict
if char in dic, means char appears twice
the index helps to determine the boundary of window
  i.e. locate faster
'''


# we need hash dict + left / right char
# use dic to track location
def my(arr):
    ans = 0  # max len
    start = 0
    dic = {}
    for end in range(len(arr)):
        # rchar start at 0
        # move rchar until len(dic) > k
        rchar = arr[end]
        if rchar in dic:
            # update start
            # in what cases start will bigger than dic[rchar] + 1 ???
            # case: aabccbb, the 2nd b
            # since current dic[rchat] is not update, and start will not change
            start = max(start, dic[rchar] + 1)
        # add/update char location
        dic[rchar] = end
        
        # update answer for each `end` index
        ans = max(ans, end - start + 1)
    return ans


# use len(set(list(str))) to check if have suplicate chars
# so if we change dic to freq dict, then only brute force code works
def non_repeat_substring(str1):
    window_start = 0
    max_length = 0
    dic = {}  # char_index_map

    # try to extend the range [windowStart, windowEnd]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        # if the map already contains the 'right_char', shrink the window from the beginning so that
        # we have only one occurrence of 'right_char'
        print(window_end, window_start, dic)

        if right_char in dic:
            # this is tricky; in the current window, we will not have any 'right_char' after its previous index
            # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
            # i.e. from 'aabccbb'
            # [w_end, w_start, dic[r_char]]:
            # [1, 1, 0]
            # [4, 4, 3]
            # [5, 4, 2]
            if window_start > dic[right_char] + 1:
                print(f'{right_char} in dic, smaller than window_start', window_start, dic[right_char] + 1)
            else:
                print(f'{right_char} in dic', window_start, dic[right_char] + 1)
            window_start = max(window_start, dic[right_char] + 1)
        # insert the 'right_char' into the map
        dic[right_char] = window_end  # update index of `right_char`
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


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
