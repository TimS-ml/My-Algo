'''
There is a dictionary containing words from an alien language for which we don't know the ordering of the alphabets.
Write a method to find the correct order of the alphabets in the alien language.
It is given that the input is a valid dictionary and there exists an ordering among its alphabets.

# Code Explain:
- Time complexity: O(V + N)
- Space complexity: O(V + N)

lc 269

Same to pp02
The only difference being that we need to build the graph of the characters by comparing adjacent words first,
and then perform the topological sort for the graph to determine the order of the characters
'''

from collections import deque


def find_order(words):
    if len(words) == 0:
        return ""

    # a. Initialize the graph
    inDegree = {}  # count of incoming edges
    graph = {}  # adjacency list graph
    for word in words:
        for character in word:
            inDegree[character] = 0
            graph[character] = []

    # b. Build the graph
    for i in range(0, len(words) - 1):
        # find ordering of characters from adjacent words
        w1, w2 = words[i], words[i + 1]
        for j in range(0, min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]
            if parent != child:  # if the two characters are different
                # put the child into it's parent's list
                graph[parent].append(child)
                inDegree[child] += 1  # increment child's inDegree
                break  # only the first different character between the two words will help us find the order

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    sortedOrder = []
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[
                vertex]:  # get the node's children to decrement their in-degrees
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # if sortedOrder doesn't contain all characters, there is a cyclic dependency between characters, therefore, we
    # will not be able to find the correct ordering of the characters
    if len(sortedOrder) != len(inDegree):
        return ""

    return ''.join(sortedOrder)


def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " +
          find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()
