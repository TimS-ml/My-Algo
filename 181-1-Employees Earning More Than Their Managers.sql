-- https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/

select e1.Name from Employee e1, Employee e2 as 'Employee'
where e1.ManagerId = e2.Id
and e1.Salary > e2.Salary