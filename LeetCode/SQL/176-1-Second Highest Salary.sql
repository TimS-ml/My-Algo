-- https://leetcode-cn.com/problems/second-highest-salary/
--  https://leetcode.com/problems/second-highest-salary/solution/
 /*
Create table If Not Exists Employee (Id int, Salary int);

insert into Employee (Id, Salary) values ('1', '100');
insert into Employee (Id, Salary) values ('2', '200');
insert into Employee (Id, Salary) values ('3', '300');
*/ -- Using max() will return a NULL if the value doesn't exist

--  SELECT max(salary) AS secondhighestsalary
--  FROM employee
--  WHERE salary <
--      (SELECT max(salary)
--       FROM employee);

-- this solution will be judged as 'Wrong Answer' if there is no such second highest salary 
-- since there might be only one record in this table
SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1

-- solution: we can take this as a temp table.
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;


-- Sol2: Using IFNULL and LIMIT clause
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
