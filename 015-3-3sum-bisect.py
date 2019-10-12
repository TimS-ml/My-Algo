# https://leetcode-cn.com/problems/3sum/


class Solution:
    def threeSum(self, nums):
        from bisect import bisect_left, bisect_right
        result = []
        length = len(nums)
        if length < 3:
            return result

        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        keys = list(count.keys())
        keys.sort()
        print(keys)

        # for numbers in count, it's count can be divided into three situations.
        # condition: num1 + num2 + num3 = 0
        # situation one: 1
        # situation two: 2, -(2 * number) must be in count if meet condition
        # situation there: >= 3, it must be zero if meet condition.
        if 0 in keys and count[0] >= 3:
            result.append([0, 0, 0])

        begin = 0
        end = bisect_left(keys, 0)

        # a只需取<0的数
        for i in range(begin, end):
            a = keys[i]
            if count[a] >= 2 and -2*a in count:
                result.append([a, a, -2*a])

            # 每个i分别计算b的范围以减小循环长度
            # a < b < c
            max_b = 0 - a // 2  # max_b可取a绝对值的一半（取整）
            min_b = 0 - a - keys[-1]  # min_b可取小于0的数or零
            # print(max_b, min_b)
            b_begin = max(i+1, bisect_left(keys, min_b))
            b_end = bisect_right(keys, max_b)

            for j in range(b_begin, b_end):
                b = keys[j]
                c = 0 - a - b
                if c in count and b <= c:
                    if b < c or count[b] >= 2:
                        result.append([a, b, c])
        return result


nums1 = [-1, 0, 1, 2, -1, -4]  # [(-1, -1, 2), (-1, 0, 1)]
nums3 = [0, 0, 0, 0]
nums4 = [-2, 0, 1, 1, 2]  # [[-2, 0, 2],[-2, 1, 1]]

print(Solution().threeSum(nums1))
