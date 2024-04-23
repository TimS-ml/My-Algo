# https://leetcode-cn.com/problems/3sum-with-multiplicity/
# https://www.cnblogs.com/stuqx/p/7291948.html


class Solution:
    def threeSumMulti(self, A, target):
        ret = 0
        count = {}
        for k in A:
            count[k] = count.get(k, 0) + 1
        print(count)

        for i in count:
            for j in count:
                k = target - i - j
                # 不然会出key error, collections.Counter(A)不会
                if i <= j and k in count:
                    if i == j == k:
                        ret += (count[i] * (count[i] - 1) * (count[i] - 2) //
                                6)
                    elif i == j != k:
                        ret += (count[i] * (count[i] - 1) * count[k] // 2)
                    elif i < j < k:
                        ret += count[i] * count[j] * count[k]
        return (int(ret) % (10**9 + 7))


A = [1, 1, 1, 3, 3, 4, 5, 5, 5]
# {1: 3, 3: 2, 4: 1, 5: 3}
target = 8
Solution().threeSumMulti(A, target)
