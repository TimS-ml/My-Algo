# https://leetcode-cn.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n):
        # s = '1'
        # for _ in range(n - 1):
        #     s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        # return s

        # def countAndSay(self, n):
        #     s = '1'
        #     for _ in range(n - 1):
        #         s = ''.join(str(len(group)) + digit
        #                     for group, digit in re.findall(r'((.)\2*)', s))
        #     return s

    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in itertools.groupby(s))
        return s


# run this:
# s = '111221'
# for digit, group in itertools.groupby(s):
#     print(digit, list(group))

print(Solution().countAndSay(5))
