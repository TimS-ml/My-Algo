-- https://leetcode-cn.com/problems/second-highest-salary/

/*
Create table If Not Exists Employee (Id int, Salary int);

insert into Employee (Id, Salary) values ('1', '100');
insert into Employee (Id, Salary) values ('2', '200');
insert into Employee (Id, Salary) values ('3', '300');
*/


-- Change the number after 'offset' gives u n-th highest salary
select (
  select distinct Salary from Employee order by Salary Desc limit 1 offset 1
)as SecondHighestSalary
