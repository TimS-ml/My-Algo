# https://leetcode-cn.com/problems/valid-anagram/
# https://blog.csdn.net/bitcarmanlee/article/details/51622263
# Counter 是一个有助于 hashable 对象计数的 dict 子类
# 它是一个无序的集合，其中 hashable 对象的元素存储为字典的键
# 它们的计数存储为字典的值，计数可以为任意整数，包括零和负数


class Solution:
    def isAnagram(self, s, t) -> bool:
        import collections
        # print(collections.Counter(s))  # Counter({'a': 2, 'c': 2})
        return collections.Counter(s) == collections.Counter(t)


# s = "anagram"
# t = "nagaram"
s = "aacc"
t = "ccac"
print(Solution().isAnagram(s, t))
