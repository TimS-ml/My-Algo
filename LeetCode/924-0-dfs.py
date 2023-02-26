'''
# Code Explain:
- Time complexity: O(N^2)
- Space complexity: O(N)

- adjacency matrix already give you
- node not sorted
- 最终的感染节点数量最小
  - 如果在一个连通子图里面, 有两个或两个以上的节点初始被感染, 那么无论我们删除哪个都对最后结果没有影响
  - 我们唯一能使感染节点减少的操作就是删除那些只有一个感染节点的连通子图中的感染节点

- 找到一个连通子图
- 判断子图中感染节点的数量，若为1，执行第三步；反之执行第一步
- 计算该子图的长度，长度越长，就越可以最小化感染节点的数量
'''


class Solution(object):
    def minMalwareSpread(self, graph, initial):
        def dfs(node, vis):
            for v in range(len(graph[node])):
                if graph[node][v] == 1 and v not in vis:
                    vis.add(v)
                    dfs(v, vis)

        s = set(initial)
        seen = set()
        del_node, subgraph_len = min(initial), 0
        for node in range(len(graph)):
            if node not in seen:
                visited = set([node])
                dfs(node, visited)

                # !!! caculate the number of infected node in the subgraph
                infect = visited & s

                if len(infect) == 1:
                    # more number of nodes or smaller index
                    if len(visited) > subgraph_len or (len(visited) == subgraph_len and
                                                   list(infect)[0] < del_node):
                        del_node, subgraph_len = list(infect)[0], len(visited)

                # https://stackoverflow.com/questions/3929278/what-does-ior-do-in-python
                # for set, it's a a union operation, add all vis to seen
                seen |= visited
        return del_node


graph = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
initial = [0, 2]
print(Solution().minMalwareSpread(graph, initial))
