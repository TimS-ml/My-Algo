'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


class Solution:
    # check if [comb of s1] is in s2
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = dict() # char needed, unchange
        win = dict()  # window freq needt
        left, right = 0, 0
        valid = 0

        # hash init
        for s in s1:
            need[s] = need.get(s, 0) + 1

        while right < len(s2):
            c = s2[right]
            right += 1

            if c in need:
                win[c] = win.get(c, 0) + 1
                if need[c] == win[c]:
                    valid += 1

            # you can change 'while' to 'if'
            while right - left >= len(s1):
                if valid == len(need):
                    return True

                d = s2[left]
                left += 1

                if d in need:
                    if win[d] == need[d]:
                        valid -= 1
                    win[d] -= 1

        return False

    def checkInclusion_2(self, s1: str, s2: str) -> bool:
        need = dict() # char needed, unchange
        win = dict()  # window freq needt
        left, right = 0, 0

        for s in s1:
            need[s] = need.get(s, 0) + 1

        while right < len(s2):
            win[s2[right]] = win.get(s2[right], 0) + 1
            if need == win:
                return True
            right += 1

            # compare
            if right - left + 1 > len(s1):
                win[s2[left]] -= 1
                if win[s2[left]] == 0:
                    del(win[s2[left]])
                left += 1

        return False
