'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


class Solution:
    def findAnagrams(self, s: str, p: str):
        need = dict() # char needed, unchange
        win = dict()  # window freq dict
        left, right = 0, 0
        valid = 0

        for c in p:
            need[c] = need.get(c, 0) + 1

        ans = []

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                win[c] = win.get(c, 0) + 1
                if need[c] == win[c]:
                    valid += 1

            while (right - left >= len(p)):
                if valid == len(need):
                    ans.append(left)

                d = s[left]
                left += 1

                if d in need:
                    if win[d] == need[d]:
                        valid -= 1
                    win[d] -= 1

        return ans

    def findAnagrams_2(self, s: str, p: str):
        need = dict() # char needed, unchange
        win = dict()  # window freq dict
        left, right = 0, 0

        for c in p:
            need[c] = need.get(c, 0) + 1

        ans = []

        while right < len(s):
            c = s[right]
            right += 1
            win[c] = win.get(c, 0) + 1

            if need == win:
                ans.appright(left)

            # compare
            if right - left + 1 > len(p):
                win[s[left]] == 0:
                    del(win[s[left]])
                left += 1
        return ans
