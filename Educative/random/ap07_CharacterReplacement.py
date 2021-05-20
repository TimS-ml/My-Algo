'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

# Pros and Cons and Notation:
'''
'''
- calc max replacement letter in sliding window
    - use freq dict to track max repleating letter in that window
    - case: aabaabbcc
    - if max replacement > k, update boundary
        - until it's == k
- how to get `maxrepl` ?
'''

def length_of_longest_substring(arr, k):
    ans = 0
    start =  0
    maxrepl = 0
    dic = {}
    for end in range(len(arr)):
        rchar = arr[end]
        dic[rchar] = dic.get(rchar, 0) + 1
        maxrepl = max(maxrepl, dic[rchar])

        # that's not correct in many means
        # while maxrepl > k:
        #     # do sth
        #     # update start
        #     lchar = arr[start]
        #     dic[lchar] -= 1
        #     # if dic[lchar] == 0:
        #     #     del dic[lchar]
        
        # what if aaaabacddd, when end at 1st d?
        #   max repl still dic[a], not changed...
        if (end - start + 1 - maxrepl) > k:
            lchar = arr[start]
            dic[lchar] -= 1  # no need to del when freq == 0
            start += 1
        ans = max(ans, end - start + 1)
    return ans

def main():
    print(length_of_longest_substring("aabaabbcc", 2))
    # print(length_of_longest_substring("aabccbb", 2))
    # print(length_of_longest_substring("abbcb", 1))
    # print(length_of_longest_substring("abccde", 1))


main()
