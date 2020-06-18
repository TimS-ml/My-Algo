# https://leetcode-cn.com/problems/perfect-squares/
# something wrong


class Solution:
    def numSquares(self, n: int) -> int:
        square = []
        j = 1
        while j * j < n:
            square.append(j * j)
            j += 1

        ans = 0
        queue = [n]
        visited = [False] * (n + 1)

        while queue:
            ans += 1
            temp = []
            for q in queue:
                for factor in square:
                    if q - factor == 0:
                        return ans
                    if q - factor < 0:
                        print('<0', q, factor)
                        break
                    if visited[q - factor]:  # boost
                        print('visited', q, factor)
                        continue
                    temp.append(q - factor)
                    print(temp, q, factor)
                    visited[q - factor] = True
                queue = temp
        return ans


n1 = 12
n2 = 4
print(Solution().numSquares(n1))
