# https://leetcode-cn.com/problems/perfect-squares/
# https://leetcode-cn.com/problems/perfect-squares/solution/python3zui-ji-chu-de-bfstao-lu-dai-ma-gua-he-ru-me/


class node:
    def __init__(self, value, step=0):
        self.value = value
        self.step = step

    def __str__(self):
        return '<value:{}, step:{}>'.format(self.value, self.step)


class Solution:
    def numSquares(self, n: int) -> int:
        queue = [node(n)]
        visited = set([node(n).value])
        # print(queue, visited)
        while queue:
            vertex = queue.pop(0)
            residuals = [
                vertex.value - n * n for n in range(1,
                                                    int(vertex.value**0.5) + 1)
            ]
            print(residuals)
            for i in residuals:
                new_vertex = node(i, vertex.step + 1)
                print(i, new_vertex)
                if i == 0:
                    return new_vertex.step
                elif i not in visited:
                    queue.append(new_vertex)
                    visited.add(i)
        return -1

    # something wrong with this solution...
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
print(Solution().numSquares(n2))
