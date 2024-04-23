class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        str = s.split()
        a = zip(pattern, str)
        return len(pattern) == len(str) and \
            len(set(a)) == len(set(pattern)) == len(set(str))
