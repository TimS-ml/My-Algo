'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''


class Solution:
    def wordBreak(self, s, wordDict):
        queue = [0]  # queue还作为终止条件
        len_list = [l for l in set(map(len, wordDict))]
        visited = [0 for _ in range(len(s) + 1)]
        while queue:
            start = queue.pop(0)
            print('start', start)
            for l in len_list:
                if s[start:start + l] in wordDict:
                    if start + l == len(s):  # segment exactly
                        return True
                    if visited[start + l] == 0:
                        # queue.pop(0)+l so that they can continue
                        queue.append(start + l)
                        print('queue', queue)
                        visited[start + l] = 1
                        print('visited', visited)
        return False


# False
s = "catsandog"
w = ["cats", "dog", "sand", "and", "cat"]

# True
s = "applepenapple"
w = ["apple", "pen"]

print(Solution().wordBreak(s, w))

