'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

/h/../  => remove h
/
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')

        ans = []
        for p in path:
            if p != '':
                if '.' in p:
                    if '..' in p and ans:
                        ans.pop()
                else:
                    ans.append(p)

        if not ans:
            return '/'

        return '/' + '/'.join(ans)
