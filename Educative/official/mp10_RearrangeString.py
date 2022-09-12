'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

lc 767
'''

from heapq import *


def rearrange_string(str):
    charFrequencyMap = {}
    for char in str:
        charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

    maxHeap = []
    # add all characters to the max heap
    for char, frequency in charFrequencyMap.items():
        heappush(maxHeap, (-frequency, char))

    previousChar, previousFrequency = None, 0
    resultString = []
    while maxHeap:
        frequency, char = heappop(maxHeap)
        # add the previous entry back in the heap if its frequency is greater than zero
        if previousChar and -previousFrequency > 0:
            heappush(maxHeap, (previousFrequency, previousChar))
        # append the current character to the result string and decrement its count
        resultString.append(char)
        previousChar = char
        previousFrequency = frequency + 1  # decrement the frequency

    # if we were successful in appending all the characters to the result string, return it
    return ''.join(resultString) if len(resultString) == len(str) else ""


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()
