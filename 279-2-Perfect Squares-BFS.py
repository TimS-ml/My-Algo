# https://leetcode-cn.com/problems/perfect-squares/
# https://leetcode-cn.com/problems/perfect-squares/solution/python3zui-ji-chu-de-bfstao-lu-dai-ma-gua-he-ru-me/


class node:
    def __init__(self,value,step=0):
        self.value = value
        self.step = step
    def __str__(self):
        return '<value:{}, step:{}>'.format(self.value,self.step)


class Solution:
    def numSquares(self, n: int) -> int:
        queue = [node(n)]
        visited = set([node(n).value])
        # print(queue, visited)
        while queue:
            vertex = queue.pop(0)
            residuals = [vertex.value-n*n for n in range(1,int(vertex.value**0.5)+1)]
            print(residuals)
            for i in residuals:
                new_vertex = node(i, vertex.step+1)
                print(i, new_vertex)
                if i==0:
                    return new_vertex.step
                elif i not in visited:
                    queue.append(new_vertex)
                    visited.add(i)                     
        return -1


n1 = 12
n2 = 4
print(Solution().numSquares(n2))
