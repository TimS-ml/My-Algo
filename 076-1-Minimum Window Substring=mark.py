# https://leetcode-cn.com/problems/minimum-window-substring/
# https://docs.python.org/3.8/library/collections.html#collections.Counter
# https://docs.python.org/3.8/library/collections.html#collections.deque
# http://book.pythontips.com/en/latest/enumerate.html


import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        score = 0
        wanted = collections.Counter(t)  # for T could be "AABC"
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
                    print(dic[letter], wanted[letter])
                    score += 1

                # in case the input is empty
                # deq: deque([0, 3, 5, 9, 10]) dic: {'A': 2, 'B': 2, 'C': 1}

                # print('S:', s[deq[0]], 'dic:', dic[s[deq[0]]],
                #       'want:', wanted[s[deq[0]]])
                while deq and dic[s[deq[0]]] > wanted[s[deq[0]]]:
                    print('==loop==')
                    # in testing case, the dic['A']==2, so while run 2 times
                    dic[s[deq.popleft()]] -= 1
                    print('after pop:', deq)

                if score == len(t) and deq[-1] - deq[0] < end - start:
                    start, end = deq[0], deq[-1]

        return s[start: end + 1]


# Output: "BANC"
S = "ADOBECODEBANC"
# T = "AABC"  # this will not trigger the while loop
T = "ABC"
print(Solution().minWindow(S, T))
