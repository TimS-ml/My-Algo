-- https://leetcode-cn.com/problems/second-highest-salary/

/*
Create table If Not Exists Employee (Id int, Salary int);

insert into Employee (Id, Salary) values ('1', '100');
insert into Employee (Id, Salary) values ('2', '200');
insert into Employee (Id, Salary) values ('3', '300');
*/


-- Using max() will return a NULL if the value doesn't exist
select max(Salary) AS SecondHighestSalary
from Employee
where Salary < (select max(Salary) from Employee);
