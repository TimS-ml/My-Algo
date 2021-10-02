'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)  # dose python provide in/out stack?

# Pros and Cons and Notation:

'''


class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = list()
        for c in s:
            if ans and ans[-1] == c:
                ans.pop()
            else:
                ans.append(c)
        return "".join(ans)

    def removeDuplicates_2(self, s: str) -> str:
        def recursion(arr):
            if len(arr) < 2:
                return arr

            for i in range(len(arr) - 1):
                if arr[i] == arr[i + 1]:
                    arr = arr.replace(arr[i] + arr[i], '')
                    return recursion(arr)
            return arr

        return recursion(s)


s = 'abbaca'
print(Solution().removeDuplicates(s))
print(Solution().removeDuplicates_2(s))
