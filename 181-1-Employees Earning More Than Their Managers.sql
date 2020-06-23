-- https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/

SELECT e1.name
FROM employee e1,
              employee e2 AS 'Employee'
WHERE e1.managerid = e2.id
  AND e1.salary > e2.salary