-- https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/

select e1.Name as 'Employee'
from  Employee e1
join Employee e2 on (e1.ManagerId = e2.Id)
where e1.Salary > e2.Salary;