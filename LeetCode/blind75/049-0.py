'''
dict in dict

{
    {freq dict}: ['eat']
    {freq dict 2}: ['cat', 'tac', ...]
}

get only the val from li

for s in li:
    freq = Freq dict for s
    update: group by freq dict

'''

import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            # speed up: avoid using sort
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

    def groupAnagrams_1(self, li):
        '''
        this is not good, you can do more optimization if char freq = 1
        for example: not using sort
        '''
        ans = {}
        for s in li:
            tok = ''.join(sorted(s))
            
            if tok in ans:
                # ans[tok] = ans[tok].append(s)  # x.append = None
                ans[tok].append(s)
            else:
                ans[tok] = [s]

            print(s, tok, ans)
        return list(ans.values())

    def groupAnagrams_2(self, li):
        def get_freq(s):
            dic = {}
            for char in s:
                dic[char] = dic.get(char, 0) + 1
            return dic

        def gen_tok(dic):
            tok = ''
            for k in sorted(dic.keys()):
                v = dic[k]
                tok = tok + str(k) + str(v)
            return tok

        ans = {}
        for s in li:
            dic = get_freq(s)
            tok = gen_tok(dic)
            
            if tok in ans:
                # ans[tok] = ans[tok].append(s)  # x.append = None
                ans[tok].append(s)
            else:
                ans[tok] = [s]

            print(s, tok, ans)
        return list(ans.values())


li = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(li))

