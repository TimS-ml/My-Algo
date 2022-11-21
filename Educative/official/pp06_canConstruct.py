'''
Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.
Unique reconstruction means that we need to find if originalSeq is the only sequence such that all sequences in the array are subsequences of it.

lc 444
same as pp03

# Code Explain:
- Time complexity: O(V + N)
- Space complexity: O(V + N)

'''

from collections import deque


def can_construct(originalSeq, sequences):
    sortedOrder = []
    if len(originalSeq) <= 0:
        return False

    # a. Initialize the graph
    inDegree = {}  # count of incoming edges
    graph = {}  # adjacency list graph
    for sequence in sequences:
        for num in sequence:
            inDegree[num] = 0
            graph[num] = []

    # b. Build the graph
    for sequence in sequences:
        for i in range(1, len(sequence)):
            parent, child = sequence[i - 1], sequence[i]
            graph[parent].append(child)
            inDegree[child] += 1

    # if we don't have ordering rules for all the numbers we'll not able to uniquely construct the sequence
    if len(inDegree) != len(originalSeq):
        return False

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        if len(sources) > 1:
            return False  # more than one sources mean, there is more than one way to reconstruct the sequence
        if originalSeq[len(sortedOrder)] != sources[0]:
            # the next source(or number) is different from the original sequence
            return False

        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[
                vertex]:  # get the node's children to decrement their in-degrees
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # if sortedOrder's size is not equal to original sequence's size, there is no unique way to construct
    return len(sortedOrder) == len(originalSeq)


def main():
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
          str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()
