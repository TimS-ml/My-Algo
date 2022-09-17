'''
# Code Explain:
- Time complexity: O(logN) (both push and pop)
- Space complexity: O(N)

lc 895

In short, we will keep three things with every number that we push to the heap:
    1. number // value of the number
    2. frequency // current frequency of the number when it was pushed to the heap
    3. sequenceNumber // a sequence number, to know what number came first
'''

from heapq import *


class Element:

    def __init__(self, number, frequency, sequenceNumber):
        self.number = number
        self.frequency = frequency
        self.sequenceNumber = sequenceNumber

    # other: Element
    def __lt__(self, other):
        # higher frequency wins
        if self.frequency != other.frequency:
            return self.frequency > other.frequency
        # if both elements have same frequency, return the element that was pushed later
        return self.sequenceNumber > other.sequenceNumber


class FrequencyStack:
    sequenceNumber = 0
    maxHeap = []
    frequencyMap = {}

    def push(self, num):
        self.frequencyMap[num] = self.frequencyMap.get(num, 0) + 1

        # Element.__lt__: for heap val comparision
        heappush(self.maxHeap,
                 Element(num, self.frequencyMap[num], self.sequenceNumber))
        self.sequenceNumber += 1

    def pop(self):
        num = heappop(self.maxHeap).number
        # decrement the frequency or remove if this is the last number
        if self.frequencyMap[num] > 1:
            self.frequencyMap[num] -= 1
        else:
            del self.frequencyMap[num]

        return num


def main():
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())


main()
