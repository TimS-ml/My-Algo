# The outer for loop runs for all characters, and the inner while loop processes each character only once
# time: O(N)
# space: O(1)


# we need hash dict + left / right char
def my(arr, k):
    ans = 0  # max len
    start = 0
    dic = {}
    for end in range(len(arr)):
        # rchar start at 0
        # move rchar until len(dic) > k
        rchar = arr[end]
        dic[rchar] = dic.get(rchar, 0) + 1

        # shrink based on k
        while len(dic) > k:
            lchar = arr[start]
            dic[lchar] -= 1
            if dic[lchar] == 0:
                del dic[lchar]
            start += 1

        ans = max(ans, end - start + 1)
    return ans


def longest_substring_with_k_distinct(str1, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    # in the following loop we'll try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
        while len(char_frequency) > k:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1  # shrink the window
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Length of the longest substr1ing: " + str(my("araaci", 2)))
    # print("Length of the longest substr1ing: " +
    #       str(longest_substring_with_k_distinct("araaci", 2)))
    # print("Length of the longest substr1ing: " +
    #       str(longest_substring_with_k_distinct("araaci", 1)))
    # print("Length of the longest substr1ing: " +
    #       str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
