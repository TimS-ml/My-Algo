'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

判断是否为有向无环图(DAG)
'''


class Solution:
    # dfs
    def canFinish(self, numCourses, prerequisites):
        def dfs(i, graph, visited):
            if visited[i] == -1:
                return True
            if visited[i] == 1:
                return False
            visited[i] = 1
            for j in graph[i]:
                if not dfs(j, graph, visited):
                    return False
            visited[i] = -1
            return True

        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        # build graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # check if DAG
        for i in range(numCourses):
            if not dfs(i, graph, visited):
                return False
        return True

    # bfs
    def canFinish_2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        outdegree = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for succ, pre in prerequisites:
            outdegree[pre].append(succ)
            indegree[succ] += 1

        queue = []
        # find start from all course - indegree == 0
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0

        while queue:
            course = queue.pop(0)
            count += 1
            for succ in outdegree[course]:
                indegree[succ] -= 1
                if indegree[succ] == 0:
                    queue.append(succ)

        # if we find all course that are equal to the given course
        return count == numCourses
