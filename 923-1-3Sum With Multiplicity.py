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
                if i <= j:  # 解决了range的问题
                    k = target - i - j
                    if k in count:
                        if i < k and k < j:
                            ret += count[i] * count[k] * count[j]
                        elif i < j and k == i:
                            ret += count[k] * (count[k] - 1) / 2 * count[j]
                        elif i < j and k == j:
                            ret += count[k] * (count[k] - 1) / 2 * count[i]
                        elif i == k and k == j:
                            ret += count[i] * (count[i] - 1) * \
                                (count[i] - 2) / 6
        return (int(ret) % (10 ** 9 + 7))


A = [1, 1, 1, 3, 3, 4, 5, 5, 5]
# {1: 3, 3: 2, 4: 1, 5: 3}
target = 8
Solution().threeSumMulti(A, target)
