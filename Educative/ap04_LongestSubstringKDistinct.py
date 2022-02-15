'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)


'''


# we need hash dict + left / right char
'''
- dynamic window size
    - loop through `end` cursor
    - when len(dic) > k, update `start`
    - update ans while looping `end`
- use a dict to save freq
    - if dic[char] == 0, del dic[char]
'''

def longest_substring_with_k_distinct(arr, k):
    ans = 0
    start = 0
    dic = {}
    for end in range(len(arr)):
        dic[arr[end]] = dic.get(arr[end], 0) + 1
        while len(dic) > k:
            print(dic)
            print(arr[end], arr[start], start)

            # my code have problem
            dic[arr[start]] -= 1
            if dic[arr[start]] == 0:
                del dic[arr[start]]
            start += 1

        ans = max(ans, end - start + 1)
    return ans


def main():
    # print("Length of the longest subarring: " + str(my("araaci", 2)))
    print("Length of the longest subarring: " +
          str(longest_substring_with_k_distinct("araaci", 2)))
    # print("Length of the longest subarring: " +
    #       str(longest_substring_with_k_distinct("araaci", 1)))
    # print("Length of the longest subarring: " +
    #       str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
