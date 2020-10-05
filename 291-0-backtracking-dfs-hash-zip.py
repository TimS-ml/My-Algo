'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

r | e | d b l u e r e d
r | e d | b l u e r e d
r | e d b | l u e r e d
r | e d b l | u e r e d
r | e d b l u | e r e d
r | e d b l u e | r e d
r | e d b l u e r | e d
r | e d b l u e r e | d
r e | d | b l u e r e d 
r e | d b | l u e r e d 
r e | d b l | u e r e d  
r e | d b l u | e r e d 
r e | d b l u e | r e d  
r e | d b l u e r | e d 
r e | d b l u e r e | d  
r e d | b | l u e r e d  
..... 

basically we extend backtracking function, now we have p and s in that function
for 'aba', len(set(s_path)) = 2

special case:
p = 'aba'
s = 'abablueaba'

p = 'twt'
s = 'ttwtt'

# Pros and Cons:
## Pros:

## Cons:

# Notation:
- similar to lc139, 140, 472
'''

class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        def dfs(p, s, p_path, s_path):
            if len(p) == len(s) == 0:
                return True
            if len(p) == 0 or len(p) > len(s):
                return False
            for i in range(len(s)):
                p_path.append(p[0])
                s_path.append(s[:i + 1])
                if len(p_path) == len(s_path) and len(set(s_path)) == len(set(p_path)) == len(set(zip(s_path, p_path))):
                    if dfs(p[1:], s[i + 1:], p_path, s_path):
                        return True
                p_path.pop()
                s_path.pop()
            return False
        return dfs(pattern, str, [], [])

"""
    - use 2 hashtables to save the exact mapping of each of the pattern charactors : portion of string
    - use recursion to try all the possibilites when we slice the remaining pattern and the remaining string
    Look at the corner case:
    p = twt
    s = ttwtt
    Be careful that for the last p = "" and s = "t", we cannot just backtrack directly 
    because t:tt was also mapped earlier in the beginning
    Therefore, we need to check if a mapping was made earlier before we backtrack
    Time    O(?) <- it is hard to determine
    Space   O(P+S)
"""

    def wordPatternMatch2(self, pattern: str, sentence: str) -> bool:
        def backtracking(p, s, forward, backward):
            if len(s) == 0 and len(p) == 0:
                return True
            if len(s) == 0 or len(p) == 0:
                return False
    
            p = p[0]
            for i in range(len(s)):
                cand = s[:i+1]
                
                # check forward mapping and backward mapping
                if p in forward and forward[p] != cand:
                    continue
                if cand in backward and backward[cand] != p:
                    continue
                
                # set mappings
                # but if that mappings existed before, rmb not to backtrack after exploration
                wasMapped = False
                if p not in forward and cand not in backward:
                    forward[p] = cand
                    backward[cand] = p
                else:
                    wasMapped = True
    
                # explore the rest of the p and sentence
                if backtracking(p[1:], s[i+1:], forward, backward):
                    return True
    
                if not wasMapped:
                    del forward[p]
                    del backward[cand]
            return False

        forward = {} # p -> sub
        backward = {} # sub ->
        ans = backtracking(p, sentence, forward, backward)
        return ans


p = "abab"
s = "redblueredblue"
print(Solution().wordPatternMatch(p, s))
