'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

- goal: longest subarr with same letters
    - find the most freq letters then replace the rest
- allowed to replace no more than k letters with any letter

!!! careful with indexing !!!
if use for loop: 
    if (r - l + 1 - maxRepl) > k:
'''

def length_of_longest_substring(arr, k):
    window = {}
    l, r = 0, 0
    ans = 0
    maxRepl = 0
    
    while r < len(arr):
        c = arr[r]
        r += 1
        window[c] = window.get(c, 0) + 1

        maxRepl = max(maxRepl, window[c])

        if (r - l - maxRepl) > k:
            d = arr[l]
            l += 1
            window[d] -= 1

        ans = max(ans, r - l)  # no +1 as well
        # print(l, r, window, maxRepl, ans)
    return ans



def main():
    # print(length_of_longest_substring("aabaabbcc", 2))
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
