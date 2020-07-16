# https://leetcode-cn.com/problems/word-break/


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


s = "applepenapple"
wordDict1 = ["apple", "pen"]
wordDict2 = ["apple", "penapple"]
print(Solution().wordBreak(s, wordDict2))
