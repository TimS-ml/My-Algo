def firstDuplicate(a):
    dic = {}
    for i in range(len(a)):
        if a[i] in dic:
            return a[i]
        else:
            dic[a[i]] = 1
    return -1

