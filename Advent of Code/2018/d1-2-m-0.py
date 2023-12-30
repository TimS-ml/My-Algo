'''
you don't need a general answer

ans[0] = 0 + n[0]
ans[1] = ans[0] + n[1] = 0 + n[0] + n[1]
ans[2] = ans[1] + n[2] = 0 + n[0] + n[1] + n[2]
...

ans[x] = ans[x-1] + n[x]

...

ans[y] = ans[y-1] + n[y] = ans[x]

-> ans[x] + n[x+1] + n[x+2] + ... + n[y] = ans[y] = ans[x]
-> n[x+1] + n[x+2] + ... + n[y] = 0
'''

from utils import grab_input

numbers = grab_input()


curr = 0
find = False
dic = set()
dic.add(curr)

while not find:
    print('Current hash length: ', len(dic))
    for i in range(len(numbers)):
        curr += numbers[i]
        if curr in dic:
            print(curr)
            find = True
            break
        dic.add(curr)

