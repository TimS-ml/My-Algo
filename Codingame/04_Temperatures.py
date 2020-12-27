# https://www.codingame.com/ide/puzzle/temperatures

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
if n == 0:
    print("0")
else:
    min = None
    for T in map(int, input().split()):
        if (min == None) or (abs(T) < abs(min)) or ((T == -min) and (T > 0)):
            min = T
    print(min)

