'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)


same as ap07
different part is:
- number of char = 2
- we don't need freq dict in this case
    - only allowed to replace `0` to `1`
    - so we just keep track the maximum number of `1` is ok
        - case: 0000001, k = 5
'''

def my(arr, k):
    ans = 0
    start =  0
    maxrepl = 0
    count1 = 0
    for end in range(len(arr)):
        if arr[end] == 1:
            count1 += 1
        maxrepl = max(maxrepl, count1)
        if (end - start + 1 - maxrepl) > k:
            if arr[start] == 1:
                count1 -= 1
            start += 1
        ans = max(ans, end - start + 1)
    return ans


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
