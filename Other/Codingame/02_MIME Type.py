# https://www.codingame.com/ide/puzzle/mime-type

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

dic = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    dic[ext.lower()] = mt

for i in range(q):
    fname = input()  # One file name per line.
    if "." not in fname:
        print("UNKNOWN")
        continue
    ext = fname.split('.')[-1].lower()
    if ext in dic:
        print(dic[ext])
    else:
        print("UNKNOWN")

# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.

