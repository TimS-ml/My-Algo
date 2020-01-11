# https://leetcode-cn.com/problems/minimum-window-substring/


import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        score = 0
        wanted = collections.Counter(t)
        start, end = len(s), len(s) * 3

        # occurance time in window
        dic = {}
        # for location of each T in S
        deq = collections.deque([])

        for num, letter in enumerate(s):
            # occurance of T in S
            if letter in wanted:
                deq.append(num)
                dic[letter] = dic.get(letter, 0) + 1
                print('deq:', deq, 'dic:', dic)
                if dic[letter] <= wanted[letter]:
                    score += 1

                # in case the input is empty
                print('S:', s[deq[0]], 'dic:', dic[s[deq[0]]],
                      'want:', wanted[s[deq[0]]])
                while deq and dic[s[deq[0]]] > wanted[s[deq[0]]]:
                    print('>')
                    # in testing case, the dic['A']==2, so while run 2 times
                    dic[s[deq.popleft()]] -= 1
                    print('after pop:', deq)

                if score == len(t) and deq[-1] - deq[0] < end - start:
                    start, end = deq[0], deq[-1]

        return s[start: end + 1]


# Output: "BANC"
S = "ADOBECODEBANC"
T = "ABC"
print(Solution().minWindow(S, T))
