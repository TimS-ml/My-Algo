-- https://leetcode-cn.com/problems/second-highest-salary/
 /*
Create table If Not Exists Employee (Id int, Salary int);

insert into Employee (Id, Salary) values ('1', '100');
insert into Employee (Id, Salary) values ('2', '200');
insert into Employee (Id, Salary) values ('3', '300');
*/ -- Change the number after 'offset' gives u n-th highest salary

SELECT
  (SELECT DISTINCT salary
   FROM employee
   ORDER BY salary DESC
   LIMIT 1
   OFFSET 1)AS secondhighestsalary