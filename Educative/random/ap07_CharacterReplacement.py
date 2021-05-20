# time: O(N)
# space: O(1)
# same as ap04
# ap04, ap05 dic is frequency dict

# key point:
# keep track of the count of the __maximum repeating letter__ in any window (let’s call it maxRepeatLetterCount).
# - we can have a window which has one letter repeating maxRepeatLetterCount times
# - this means we should try to replace the remaining letters.
# - If we have more than ‘k’ remaining letters
#   - __shrink the window__ as we are not allowed to replace more than ‘k’ letters


def length_of_longest_substring(str1, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    dic = {}  # frequency_map

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        # if right_char not in dic:
        #     dic[right_char] = 0
        # dic[right_char] += 1
        dic[right_char] = dic.get(right_char, 0) + 1
        max_repeat_letter_count = max(max_repeat_letter_count,
                                      dic[right_char])

        # Current window size is from window_start to window_end, overall we have a letter which is
        # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
        # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
        # if the remaining letters are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' letters
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str1[window_start]
            dic[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
