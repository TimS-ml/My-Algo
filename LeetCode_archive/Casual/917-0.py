'''
# Code Explain:
- Time complexity: O()
- space complexity: O()



case: s = "a-bC-dEf-ghIj"
out :     "j-Ih-gfE-dCba"

case: s = "Test1ng-Leet=code-Q!"
out :     "Qedo1ct-eeLg=ntse-T!"
number's position not changed

- locate and save char's location (might be [])
- reverse string
- generate answer string
'''


class solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # s = list(s)
        # rev = s[::-1]
        # i, rev_i = 0, 0
        # L = len(s)

        # while True:
        #     while i < L and not s[i].isalpha():
        #         i += 1
        #     while rev_i < L and not rev[rev_i].isalpha():
        #         rev_i += 1
        #     if i < L and rev_i < L:
        #         s[i] = rev[rev_i]
        #         i += 1
        #         rev_i += 1
        #     else:
        #         break
        # return ''.join(s)

        ans = []
        j = len(ans) - 1
        for _, x in enumerate(s):
            if x.isalpha():
                while not s[j].isalpha():
                    j -= 1
                ans.append(s[j])
                j -= 1
            else:
                ans.append(x)

        return ''.join(ans)

    def reverseOnlyLetters_2(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return ''.join(ans)
