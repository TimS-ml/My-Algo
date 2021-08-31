-- https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/

--  Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, ManagerId int)
--  Truncate table Employee
--  insert into Employee (Id, Name, Salary, ManagerId) values ('1', 'Joe', '70000', '3')
--  insert into Employee (Id, Name, Salary, ManagerId) values ('2', 'Henry', '80000', '4')
--  insert into Employee (Id, Name, Salary, ManagerId) values ('3', 'Sam', '60000', 'None')
--  insert into Employee (Id, Name, Salary, ManagerId) values ('4', 'Max', '90000', 'None')


SELECT e1.name
FROM employee e1,
              employee e2 AS 'Employee'
WHERE e1.managerid = e2.id
  AND e1.salary > e2.salary



SELECT e1.name AS 'Employee'
FROM employee e1
JOIN employee e2 ON (e1.managerid = e2.id)
WHERE e1.salary > e2.salary;
