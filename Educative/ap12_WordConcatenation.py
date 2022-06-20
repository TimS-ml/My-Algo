'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

lc 30
ap09 just replace single char to a word

String="catoxcat", Words=["cat", "tox"]
return [2]

String="catscat", Words=["cat", "cats"] => cats + cat
return [0]
'''

def find_word_concatenation(arr, words):
    freqArr, freqWord = {}, {}
    for w in words:
        freqWord[w] = freqWord.get(w, 0) + 1

    l, r = 0, 0
    valid = 0
    ans = []
    while r < len(arr):
        w = arr[r]
        r += 1

        if w in freqWord:
            freqArr[w] = freqArr.get(w, 0) + 1

            if freqArr[w] == freqWord[w]:
                valid += 1

        if valid == len(freqWord):
            ans.append(l)

        if r >= len(words):
            d = arr[l]
            l += 1

            if d in freqWord:
                if freqArr[d] == freqWord[d]:
                    valid -= 1
                freqArr[d] -= 1

    return ans

