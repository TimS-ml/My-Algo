'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

case:
String="xxabdbca", Pattern="ac"
[1] move r xxabdbc
[2] move l abdbc
[3] move r abdbca
[4] move l ca
'''

def find_substring(arr, pattern):
    freqArr, freqPattern = {}, {}
    for c in pattern:
        freqPattern[c] = freqPattern.get(c, 0) + 1

    l, r = 0, 0
    valid = 0
    ans = ''
    while r < len(arr):
        c = arr[r]
        r += 1

        if c in freqPattern:
            freqArr[c] = freqArr.get(c, 0) + 1

            if freqArr[c] == freqPattern[c]:
                valid += 1

        if valid == len(freqPattern):
            if ans == '' or r - l < len(ans):
                ans = arr[l:r]
            # print(ans)

        # use different shrink rule
        # [1] find available r
        # [2] shrink available l => reset freqDict etc.
        # You need to be able to go back to last succeful l
        # if ans != '':
        #     print('before: ', l, freqArr)
        
        if valid == len(freqPattern):
            while l <= r:
                d = arr[l]
                l += 1
    
                if d in freqPattern:
                    if freqArr[d] == freqPattern[d]:
                        l -= 1  # go back
                        break
                    else:
                        freqArr[d] -= 1
    
                if r - l < len(ans):
                    ans = arr[l:r]
                    # print(ans)

        # if ans != '':
        #     print('after: ', l, freqArr)
    return ans


print(find_substring("aabdec", "abc"))
print(find_substring("aabdec", "abac"))
print(find_substring("abdbca", "abc"))
print(find_substring("adcad", "abc"))
