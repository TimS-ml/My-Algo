'''
case

T ([])
F ([)]
    when )
    if ] or } or ( alowed
    if ) or [ or {
    
F ())

stack

'''

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', 
               ']': '[', 
               '}': '{'}
        
        stack = []
        
        s = list(s)
        for i in range(len(s)):
            # if s[i] in ['{', '(', '[']:
            if s[i] not in dic:  # left
                stack.append(s[i])
            else:
                if not stack:  # ))
                    return False
                top = stack[-1]
                if dic[s[i]] == top:  # pair
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False
