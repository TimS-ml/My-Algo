'''
# Code Explain:
both dfs and bfs
- Time complexity: O(n)
- Space complexity: O(n)

# Pros and Cons and Notation:
One employee has at most one direct leader and may have several subordinates.

input is a list of type 'Employee'
    - e[i].id
    - e[i].importance
    - e[i].subordinates

- we want to loop by id
    - build a hash table

in dfs recursion make sure that 'depth first'
in bfs que.popleft() make sure that 'breadth first'
'''

from typing import List
from collections import deque


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance_dfs(self, employees: List['Employee'], idx: int) -> int:
        dic = {e.id: e for e in employees}

        def dfs(idx):
            curr_employee = dic[idx]
            ans = curr_employee.importance + sum(
                dfs(sub_idx) for sub_idx in curr_employee.subordinates)
            return ans

        return dfs(idx)

    def getImportance_bfs(self, employees: List['Employee'], idx: int) -> int:
        dic = {e.id: e for e in employees}

        ans = 0
        que = deque([idx])
        while que:
            curr_employee = dic[que.popleft()]
            ans += curr_employee.importance
            for sub_idx in curr_employee.subordinates:
                que.append(sub_idx)

        return ans


# actually this is not what the input looks like...
employees_raw = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
idx = 1

employees = [Employee(e[0], e[1], e[2]) for e in employees_raw]
print(Solution().getImportance_dfs(employees, idx))
print(Solution().getImportance_bfs(employees, idx))
