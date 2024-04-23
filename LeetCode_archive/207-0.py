'''
# Code Explain:
- Time complexity: O(V + E)
- Space complexity: O(V + E)
dependencies + number of courses
E = num of edges
V = num of vertices

判断是否为有向无环图(DAG)

visited must have -1 and 1 and 0 three types of the state
in sol 1:
v[x] = 1 means visiting
v[x] = -1 means done visit and is ok
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

        # build graph, single direction
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # check if DAG
        # the reason we need three visited states is because this for loop!!!
        for i in range(numCourses):
            if not dfs(i, graph, visited):
                return False
        return True

    # dfs
    def canFinish_2(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crouse, pre in prerequisites:
            graph[crouse].append(pre)

        visiting = set()

        def dfs(crouse):
            if crouse in visiting:
                return False
            if graph[crouse] == []:
                return True

            visiting.add(crouse)
            for pre in graph[crouse]:
                if not dfs(pre):
                    return False
            visiting.remove(crouse)

            # since there gonna be start at each points dfs separately, so this is ok
            graph[crouse] = []  # that's how this solution mark second states
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

    # bfs
    def canFinish_3(self, numCourses, prerequisites):
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
