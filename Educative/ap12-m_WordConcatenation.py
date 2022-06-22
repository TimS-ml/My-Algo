'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

All words are of the same length!!!

lc 30
fix windows size, double ap01

String="catoxcat", Words=["cat", "tox"]
return [2]

Follow up: unfix length
String="catscat", Words=["cat", "cats"] => cats + cat
return [0]
'''


def find_word_concatenation(arr, words):
    ans = []
    return ans


# just for fun... put the pointer at end of window
def find_word_concatenation_2(arr, words):
    freqWord = {}
    for w in words:
        freqWord[w] = freqWord.get(w, 0) + 1

    windowSize = len(words) * len(words[0])
    wordSize = len(words[0])
    i = len(words) * len(words[0]) - 1  # window end idx
    ans = []
    while i < len(arr):
        window = arr[i - windowSize + 1: i + 1]
        freqArr = {}
        j = len(words[0]) - 1  # sub window end idx
        valid = 0

        # print(window)
        while j < len(window):
            w = window[j - wordSize + 1: j + 1]
            
            if w in freqWord:
                freqArr[w] = freqArr.get(w, 0) + 1

                if freqArr[w] == freqWord[w]:
                    valid += 1
            else:
                break

            j += wordSize

        if valid == len(freqWord):
            ans.append(i - windowSize + 1)

        i += 1

    return ans


def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()
