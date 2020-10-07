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

in sol1, we pass 2 path (list)
in sol2, we pass 2 hashmap (dict)

special case:
p = 'aba'
s = 'abablueaba'

p = 'twt'
s = 'ttwtt'

sol2:
use recursion to try all the possibilites when we slice the remaining pattern and the remaining string
Look at the corner case 'twt' and 'ttwtt':
- Be careful that for the last p = "" and s = "t", we cannot just backtrack directly 
- because t:tt was also mapped earlier in the beginning
Therefore, we need to check if a mapping was made earlier before we backtrack

# Pros and Cons:
## Pros:

## Cons:

# Notation:
- similar to lc139, 140, 472

'''

import pysnooper


@pysnooper.snoop()
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
                if len(p_path) == len(s_path) and len(set(s_path)) == len(
                        set(p_path)) == len(set(zip(s_path, p_path))):
                    if dfs(p[1:], s[i + 1:], p_path, s_path):
                        return True
                p_path.pop()
                s_path.pop()
            return False

        return dfs(pattern, str, [], [])

    def wordPatternMatch2(self, pattern: str, str: str) -> bool:
        def backtracking(p, s, forward, backward):
            if len(s) == 0 and len(p) == 0:
                return True
            if len(s) == 0 or len(p) == 0:
                return False

            p_pat = p[0]
            for i in range(len(s)):
                c_pat = s[:i + 1]

                # check forward mapping and backward mapping
                if p_pat in forward and forward[p_pat] != c_pat:
                    continue
                if c_pat in backward and backward[c_pat] != p_pat:
                    continue

                # set mappings
                # but if that mappings existed before, rmb not to backtrack after exploration
                mapped = False
                if p_pat not in forward and c_pat not in backward:
                    forward[p_pat] = c_pat
                    backward[c_pat] = p_pat
                else:
                    mapped = True

                # explore the rest of the pattern and sentence
                if backtracking(p[1:], s[i + 1:], forward, backward):
                    return True

                # after backtracking return False
                # if was mapped, then not del
                if not mapped:
                    del forward[p_pat]
                    del backward[c_pat]
            return False

        forward = {}  # p -> sub
        backward = {}  # sub -> p
        ans = backtracking(pattern, str, forward, backward)
        return ans


p = "abab"
s = "redblueredblue"
print(Solution().wordPatternMatch2(p, s))
