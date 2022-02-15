'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)



same as ap07
number of char = 2
we don't need freq dict in this case since we only allowed to replace 0 to 1
and thus, no need to update max_repeat_letter_count, 
  since dic[right_char] and max_repeat_letter_count are the same 
max_repeat_letter_count = max(max_repeat_letter_count,
                          dic[right_char])
'''


def length_of_longest_substring(arr, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_repeat_letter_count += 1  # count for one

        # Current window size is from window_start to window_end, overall we have a maximum of 1s
        # repeating 'max_repeat_letter_count' times, this means we can have a window with 'max_repeat_letter_count' 1s
        # and the remaining are 0s which should replace with 1s.
        # now, if the remaining 0s are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' 0s
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            if arr[window_start] == 1:
                max_repeat_letter_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(length_of_longest_substring(
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
