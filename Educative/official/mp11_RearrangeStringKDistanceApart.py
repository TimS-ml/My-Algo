'''
# Code Explain:
- Time complexity: O(NlogN)
- Space complexity: O(N)

re-insert the character after K iterations
'''

from heapq import *
from collections import deque


def reorganize_string(str, k):
    if k <= 1:
        return str

    charFrequencyMap = {}
    for char in str:
        charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

    maxHeap = []
    # add all characters to the max heap
    for char, frequency in charFrequencyMap.items():
        heappush(maxHeap, (-frequency, char))

    queue = deque()
    resultString = []
    while maxHeap:
        frequency, char = heappop(maxHeap)
        # append the current character to the result string and decrement its count
        resultString.append(char)

        # !!! decrement the frequency and append to the queue
        # so you don't need a counter for each individual vars
        queue.append((char, frequency + 1))
        if len(queue) == k:
            char, frequency = queue.popleft()
            if -frequency > 0:
                heappush(maxHeap, (frequency, char))

    # if we were successful in appending all the characters to the result string, return it
    return ''.join(resultString) if len(resultString) == len(str) else ""


def main():
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))


main()
