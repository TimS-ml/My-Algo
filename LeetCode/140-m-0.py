'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wd = set(wordDict)

        cache = {}

        # def recur(idx, path):
        #     if idx == len(s) - 1:
        #         ans.append(' '.join(path))
        #         return

        #     for w in wd:
        #         if len(w) + idx <= len(s) - 1:
        #             path.append(w)
        #             recur(idx + len(w), path)
        #             path.pop()

        # func(path) -> new path
        def recur(path):
            if path in cache:
                return cache[path]
            if not path:
                return [[]]

            for w in wd:
                if w == s[:len(w)]:
                    path.append(w)
                    for substr in recur(path):
                        cache[path].append(substr)
                    path.pop()

            return cache[path]

        recur(s)

        return [' '.join(words) for words in cache[s]]
