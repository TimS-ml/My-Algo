'''
We need to print all possible ordering of tasks meeting all prerequisites

# Code Explain:
- Time complexity: O(V! + E)
- Space complexity: O(V! + E)

# Pros and Cons and Notation:
At any stage, if we have more than one source available and since we can choose any source, therefore, in this case, we will have multiple orderings of the tasks. 
We can use a recursive approach with Backtracking to consider all sources at any step.
'''

from collections import deque


def print_orders(tasks, prereqs):
    ans = []

    # we need 2 hash dict:
    # [1] key is child
    # count of in degrees (number of connection to that node) => for popup order usage
    inDegree = {i: 0 for i in range(tasks)}

    # [2] key is parent
    # list of out node(s) => for connection usage
    graph = {i: [] for i in range(tasks)}

    # [3] list of head
    sources = deque()

    for edge in prereqs:
        parent, child = edge[0], edge[1]
        inDegree[child] += 1
        graph[parent].append(child)

    for child in inDegree:
        if inDegree[child] == 0:
            sources.append(child)  # then this child is an orphan

    # BFS
    def bfs(sources, ans):
        if sources:
            for curr_source in sources:
                ans.append(curr_source)
                sources_next = deque(sources)
                sources_next.remove(curr_source)
                for child in graph[curr_source]:
                    inDegree[child] -= 1
                    # update `source`
                    if inDegree[child] == 0:
                        sources_next.append(child)

                bfs(sources_next, ans)

                ans.remove(curr_source)
                for child in graph[curr_source]:
                    inDegree[child] += 1

        # why based on num of connection ???
        if len(ans) == len(inDegree):
            print(ans)

    bfs(sources, ans)


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
