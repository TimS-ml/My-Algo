'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

def find_permutation(arr, pattern):
    freqArr, freqPattern = {}, {}
    for c in pattern:
        freqPattern[c] = freqPattern.get(c, 0) + 1

    l, r = 0, 0
    valid = 0
    while r < len(arr):
        c = arr[r]
        r += 1

        if c in freqPattern:
            freqArr[c] = freqArr.get(c, 0) + 1

            if freqArr[c] == freqPattern[c]:
                valid += 1

        if valid == len(freqPattern):
            return True

        if r >= len(pattern):
            d = arr[l]
            l += 1

            if d in freqPattern:
                if freqArr[d] == freqPattern[d]:
                    valid -= 1
                freqArr[d] -= 1

    return valid == len(freqPattern)



def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' +
          str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
