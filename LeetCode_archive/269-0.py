'''
# Code Explain:
- Time complexity: O(C)
C is the total length of all word of chars = V + E
- Space complexity: O(1)

Total Length is unknown

Make sure:
[1] all connected
not work: a->b, c->
[2] no loop
not work:
|-<<-|
a->b->c

What if multi-brunch? Post order!!!
|->>-|
a->b->c

with multiple path states to tell what kind of loop is not valid
'''

from typing import List
from collections import defaultdict, Counter, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # for word in words, for char in word
        graph = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # only add the first different char
                    # case: 'azz', 'ba'  -> a > b
                    # case: 'abd', 'abk' -> d > k
                    print(w1[j], w2[j])
                    graph[w1[j]].add(w2[j])
                    break

        visited = {}  # {char: bool} False visited, True current path
        ans = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in graph[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            ans.append(char)  # post order

        for char in graph:
            if dfs(char):
                return ""

        ans.reverse()
        return "".join(ans)


    def alienOrder_2(self, words: List[str]) -> str:
        # Step 0: Put all unique letters into the adj list.
        reverse_adj_list = {c : [] for word in words for c in word}
    
        # Step 1: Find all edges and put them in reverse_adj_list.
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d: 
                    reverse_adj_list[d].append(c)
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): 
                    return ""
    
        # Step 2: Depth-first search.
        seen = {} # False = grey, True = black.
        output = []
        def visit(node):  # Return True iff there are no cycles.
            if node in seen:
                return seen[node] # If this node was grey (False), a cycle was detected.
            seen[node] = False # Mark node as grey.
            for next_node in reverse_adj_list[node]:
                result = visit(next_node)
                if not result: 
                    return False # Cycle was detected lower down.
            seen[node] = True # Mark node as black.
            output.append(node)
            return True
    
        if not all(visit(node) for node in reverse_adj_list):
            return ""
    
        return "".join(output)


    # bfs
    def alienOrder_3(self, words: List[str]) -> str:
        
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})
                
        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""
        
        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)
                    
        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)
