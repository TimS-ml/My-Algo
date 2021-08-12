'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

'''

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        score = 0

        wanted = collections.Counter(t)  # for T could be "AABC"
        start, end = len(s), len(s) * 3  # ans location, set a big init number

        # 'number of occurances' for every T in S
        dic = {}
        # 'occurances location' for every T in S
        deq = collections.deque([])

        for num, letter in enumerate(s):
            # occurance of T in S
            if letter in wanted:
                deq.append(num)
                dic[letter] = dic.get(letter, 0) + 1
                # print('deq:', deq, 'dic:', dic)
                if dic[letter] <= wanted[letter]:
                    score += 1
                    print("letter:{}, dic:{} <= wanted:{}, score:{}".format(
                        letter, dic[letter], wanted[letter], score))
                else:
                    print("letter:{}, {} > {}, score:{}".format(
                        letter, dic[letter], wanted[letter], score))

                # deq: deque([0, 3, 5, 9, 10]) dic: {'A': 2, 'B': 2, 'C': 1}
                while deq and dic[s[deq[0]]] > wanted[s[deq[0]]]:
                    print("s:{}, dic[s]:{}, want[s]:{}".format(
                        s[deq[0]], dic[s[deq[0]]], wanted[s[deq[0]]]))
                    # in testing case, the dic['A']==2, so 'while' will loop 2 times
                    dic[s[deq.popleft()]] -= 1
                    print("after pop, deq:{}, dic:{}".format(deq, dic))

                # so in which case score != len(t) ???
                if score == len(t) and deq[-1] - deq[0] < end - start:
                    print("=> ANS: {}-{} < {}-{}".format(
                        deq[-1], deq[0], end, start))
                    start, end = deq[0], deq[-1]

        return s[start:end + 1]


# Output: "BANC"
S = "ADOBECODEBANC"
T = "AABC"  # this will not trigger the while loop
# T = "ABC"
print(Solution().minWindow(S, T))
