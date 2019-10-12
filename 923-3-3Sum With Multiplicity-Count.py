# https://leetcode-cn.com/problems/3sum-with-multiplicity/
# https://www.cnblogs.com/stuqx/p/7291948.html


import collections


class Solution:
    def threeSumMulti(self, A, target):
        ret = 0
        count = collections.Counter(A)
        # Counter({1: 3, 5: 3, 3: 2, 4: 1})
        print(count)
        # print('count[6]', count[6])  # 输出是0不是key error，很有意思

        for i in count.keys():
            for j in count.keys():
                k = target - (i + j)  # 也不用考虑k是不是再count里，元组
                print(k)
                if i == j == k:
                    print(i, j, k, 'i == j == k')
                    ret += (count[i] * (count[i]-1) * (count[i]-2) // 6)
                    print('ret', ret, '\n')
                elif i == j != k:
                    print(i, j, k, 'i == j != k')
                    ret += (count[i] * (count[i]-1) * count[k] // 2)
                    print('ret', ret, '\n')
                elif i < j < k:
                    print(i, j, k, 'i < j < k')
                    ret += count[i] * count[j] * count[k]
                    print('ret', ret, '\n')
        return ret % 1000000007


A = [1, 1, 1, 3, 3, 4, 5, 5, 5]
# {1: 3, 3: 2, 4: 1, 5: 3}
target = 8
Solution().threeSumMulti(A, target)
