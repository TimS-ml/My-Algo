from collections import Counter


def firstNotRepeatingCharacter(s):
    dic = Counter(s)
    for i in range(len(s)):
        if dic[s[i]] == 1:
            return s[i]
    return '_'
