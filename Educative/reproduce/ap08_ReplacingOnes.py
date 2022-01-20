'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

# Pros and Cons and Notation:
'''
'''
same as ap07
different part is:
- number of char = 2
- we don't need freq dict in this case
    - only allowed to replace 0 to 1
    - so we just keep track the maximum number of 1 is ok
        - case: 0000001, k = 5
'''

def length_of_longest_substring(arr, k):
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


def main():
    print(length_of_longest_substring(
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
