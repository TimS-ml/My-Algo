'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

A building has an ocean view if 
all the buildings to its right have a smaller (h >= h_right) height.


# Brute force
Time O(n^2)
function tallest(start):
    return tallest building in li[start+1:]

tallest_li = [tallest(li, i) for i in range xxx]
compare if li[i] > tallest_li(i)


# Stack
Know ans[-1] = 1

Loop reverslly, we should ideally found an increasing seq
Just mark the non increasing seq idx
'''

