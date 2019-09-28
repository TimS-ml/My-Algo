# https://leetcode-cn.com/problems/rabbits-in-forest/


class Solution:
    def numRabbits(self, answers):
        count = {}
        ans = 0
        for i in answers:
            count[i] = count.get(i, 0) + 1
        # print(count)

        for key, value in count.items():
            print(key, value)
            if key == 0:
                ans += value
            elif key == 1:  # [3, 3, 3]
                tmp = value // (key+1)
                # print('tmp1', tmp)
                ans += (tmp+1)*(key+1)
            else:  # [3, ...., 3] k=3 v=13 (>4*3)
                tmp = value // (key+1)
                # print('tmp2', tmp)
                ans += (tmp+1)*(key+1)
        return ans


ans0 = []
ans1 = [10, 10, 10]
ans2 = [1, 1, 2]
ans3 = [0, 0, 1, 1, 1]
ans4 = [0, 1, 0, 2, 0, 1, 0, 2, 1, 1]
print('ans', Solution().numRabbits(ans2))
