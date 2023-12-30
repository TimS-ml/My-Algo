'''
ans[0] = 0 + n[0]
ans[1] = ans[0] + n[1] = 0 + n[0] + n[1]
ans[2] = ans[1] + n[2] = 0 + n[0] + n[1] + n[2]
...
'''

from utils import *

numbers = grab_input()


# [1] using numpy
# import numpy as np
# ans = np.cumsum(numbers)
# ans = ans.tolist()

# [2] using functools.reduce
# from functools import reduce
# 
# # Helper function to append the sum to the list
# def cumulative_sum(acc, x):
#     acc.append(acc[-1] + x if acc else x)
#     return acc
# 
# ans = reduce(cumulative_sum, numbers, [])

# [3] using itertools.accumulate
import itertools
ans = list(itertools.accumulate(numbers))


print(ans)
