-- https://leetcode-cn.com/problems/second-highest-salary/
 /*
Create table If Not Exists Employee (Id int, Salary int);

insert into Employee (Id, Salary) values ('1', '100');
insert into Employee (Id, Salary) values ('2', '200');
insert into Employee (Id, Salary) values ('3', '300');
*/ -- Using max() will return a NULL if the value doesn't exist

SELECT max(salary) AS secondhighestsalary
FROM employee
WHERE salary <
    (SELECT max(salary)
     FROM employee);

