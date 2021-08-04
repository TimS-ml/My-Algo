def isCryptSolution(crypt, solution):
    dic = {ord(c): d for c, d in solution}
    *v, = map(lambda x: x.translate(dic), crypt)
    return not any(x != "0" and x.startswith("0") for x in v) and \
        int(v[0]) + int(v[1]) == int(v[2])


def isCryptSolution_2(crypt, solution):
    table = str.maketrans(dict(solution))
    t = tuple(s.translate(table) for s in crypt)
    zeroes = any(s[0] == '0' for s in t if len(s) > 1)
    return not zeroes and int(t[0]) + int(t[1]) == int(t[2])


def isCryptSolution_3(crypt, solution):
    dic = {i[0]: int(i[1]) for i in solution}
    c0 = crypt[0]
    c1 = crypt[1]
    c2 = crypt[2]

    L = len(c2)
    Li, Lj = len(c0), len(c1)

    if (dic[c0[0]] == 0 and Li != 1) or \
       (dic[c1[0]] == 0 and Lj != 1) or \
       (dic[c2[0]] == 0 and L != 1):
        return False

    L = len(c2)
    Li, Lj = len(c0), len(c1)
    if L < Li or L < Lj:
        return False

    sum0, sum1, sum2 = 0, 0, 0
    i, j, k = 0, 0, 0

    while k < L:
        if i < Li:
            sum0 = sum0 * 10 + dic[c0[i]]
            i += 1

        if j < Lj:
            sum1 = sum1 * 10 + dic[c1[j]]
            j += 1

        sum2 = sum2 * 10 + dic[c2[k]]
        k += 1

    return sum0 + sum1 == sum2
