class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    dic1, dic2 = {}, {}
    if len(s) != len(t):
      return False
    for i in range(len(s)):
      dic1[s[i]] = dic1.get(s[i], 0) + 1
      dic2[t[i]] = dic2.get(t[i], 0) + 1
    return dic1 == dic2

