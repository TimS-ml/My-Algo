'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

same as ap09, but return string idx
'''

def find_string_anagrams(arr, pattern):
    freqArr, freqPattern = {}, {}
    for c in pattern:
        freqPattern[c] = freqPattern.get(c, 0) + 1

    l, r = 0, 0
    valid = 0
    ans = []
    while r < len(arr):
        c = arr[r]
        r += 1

        if c in freqPattern:
            freqArr[c] = freqArr.get(c, 0) + 1

            if freqArr[c] == freqPattern[c]:
                valid += 1

        if valid == len(freqPattern):
            ans.append(l)

        if r >= len(pattern):
            d = arr[l]
            l += 1

            if d in freqPattern:
                if freqArr[d] == freqPattern[d]:
                    valid -= 1
                freqArr[d] -= 1

    return ans


print(find_string_anagrams("ppqp", "pq"))
print(find_string_anagrams("abbcabc", "abc"))
