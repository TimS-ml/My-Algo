'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

[1] Base State
[2] State Transfer Equation
[3] Initialize Conditions
[4] State Compression (optional)
[5] Terminate Conditions
'''


class Solution:
    # 前缀递推
    # 先计算包含 s2 的前缀子串的窗口, 再根据前缀子串窗口不断拓展, 找到包含整个字符串的窗口. 
    def minWindow_1(self, s1: str, s2: str) -> str:
        cur = [-1] * len(s1)
        # save the positions of all s2[0] in s1
        for i, m_char in enumerate(s1):
            if m_char == s2[0]:
                cur[i] = i

        # 遍历s2中所有的字符, 不断找到s2中所有字符在s1中出现的所有位置
        for j in range(1, len(s2)):
            # last 用来标记s2上一个字符最后出现的位置
            last = -1
            # new 用来标记上一个字符s2[j - 1]在s1中出现的所有位置
            new = [-1] * len(s1)
            for i, m_char in enumerate(s1):
                # 由于我们需要保证s2字符的顺序, 因此只有在上一个字符出现过
                #   然后当前字符出现的情况下, 才会记录上一个字符字符的位置
                # 这样能够保证所有s2字符都在s1中, 以正确的顺序出现
                if last != -1 and m_char == s2[j]:
                    new[i] = last
                if cur[i] != -1:
                    last = cur[i]
            cur = new

        # 到这里时, cur[i]中存储的元素(在!=-1时)代表:
        #   以s1[i]为终点的最小窗口子序列的起点坐标
        start, end = 0, len(s1)
        for end_index, start_index in enumerate(cur):
            if start_index >= 0 and end_index - start_index < end - start:
                start, end = start_index, end_index
        return s1[start:end + 1] if end < len(s1) else ""

    # next 数组
    # def minWindow_2(self, s1: str, s2: str) -> str:
    #     N = len(s1)
    #     next = [None] * N
    #     last = [-1] * 26
    #     for i in range(N - 1, -1, -1):
    #         last[ord(s1[i]) - ord('a')] = i
    #         next[i] = tuple(last)

    #     windows = [[i, i] for i, c in enumerate(s1) if c == s2[0]]
    #     for j in range(1, len(s2)):
    #         letter_index = ord(s2[j]) - ord('a')
    #         windows = [[root, next[i + 1][letter_index]] for root, i in windows
    #                    if 0 <= i < N - 1 and next[i + 1][letter_index] >= 0]

    #     if not windows: return ""
    #     i, j = min(windows, key=lambda (i, j): j - i)
    #     return s1[i:j + 1]
