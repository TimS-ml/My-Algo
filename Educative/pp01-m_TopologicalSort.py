'''
Given a directed graph(a graph with unidirectional edges), find the topological ordering of its vertices.

# Code Explain:
- Time complexity: O(V + E)
- Space complexity: O(V + E)


A topological ordering starts with one of the sources and ends at one of the sinks
A topological ordering is possible only when the graph has no directed cycles

BFS
We will start with all the sources, and in a stepwise fashion, save all sources to a sorted list. 
We will then remove all sources and their edges from the graph. 
After the removal of the edges, we will have new sources, so we will repeat the above process until all vertices are visited.
'''
'''
[a] Initialization
We will store the graph in Adjacency Lists, 
    which means each parent vertex will have a list containing all of its children. 
    We will do this using a HashMap where the ‘key’ will be the parent vertex number and the value will be a List containing children vertices.
To find the sources, we will keep a HashMap to count the in-degrees 
    i.e., count of incoming edges of each vertex. Any vertex with ‘0’ in-degree will be a source.

[b] Build the graph and find in-degrees of all vertices
We will build the graph from the input and populate the in-degrees HashMap.

[c] Find all sources
All vertices with ‘0’ in-degrees will be our sources and we will store them in a Queue.

[d] Sort
For each source, do the following things:
    Add it to the sorted list.
    Get all of its children from the graph.
    Decrement the in-degree of each child by 1.
    If a child’s in-degree becomes ‘0’, add it to the sources Queue.
Repeat until the source Queue is empty.
'''

from collections import deque


# assume v >=0
def topological_sort(v, e):
    ans = []

    # we need 2 hash dict:
    # [1] key is child
    # count of in degrees (number of connection to that node) => for popup order usage
    inDegree = {i: 0 for i in range(v)}

    # [2] key is parent
    # list of out node(s) => for connection usage
    graph = {i: [] for i in range(v)}

    # [3] list of head
    sources = deque()

    for edge in e:
        parent, child = edge[0], edge[1]
        inDegree[child] += 1
        graph[parent].append(child)

    for child in inDegree:
        if inDegree[child] == 0:
            sources.append(child)  # then this child is an orphan

    # BFS
    # How does the `sources` update?
    while sources:
        curr_source = sources.popleft()
        ans.append(curr_source)
        for child in graph[curr_source]:
            inDegree[child] -= 1
            # update `source`
            if inDegree[child] == 0:
                sources.append(child)

    # !!! Detect if is DAG
    if len(ans) != v:
        return []

    return ans


def main():
    # Vertices, Edges
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " + str(
        topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1],
                             [3, 2], [4, 1]])))


main()
