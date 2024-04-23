'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()


There is at least one word in s

sol 2:
s[::-1]
'neeuq gard evol I'

s[::-1].split(" ")
['neeuq', 'gard', 'evol', 'I']

s[::-1].split(" ")[::-1]
['I', 'evol', 'gard', 'neeuq']

" ".join(s[::-1].split(" ")[::-1])
'I evol gard neeuq'
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split()
        for i in range(len(li)):
            li[i] = li[i][::-1]
        return ' '.join(li)

    def reverseWords_2(self, s: str) -> str:
        return " ".join(s[::-1].split(" ")[::-1])
