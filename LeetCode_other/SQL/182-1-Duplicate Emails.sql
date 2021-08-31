-- https://leetcode-cn.com/problems/duplicate-emails/
-- check question 196

--  Create table If Not Exists Person (Id int, Email varchar(255))
--  Truncate table Person
--  insert into Person (Id, Email) values ('1', 'a@b.com')
--  insert into Person (Id, Email) values ('2', 'c@d.com')
--  insert into Person (Id, Email) values ('3', 'a@b.com')

SELECT email
FROM
  (SELECT email,
          count(email) AS num
   FROM person
   GROUP BY email) AS statistic
WHERE num > 1;


SELECT email
FROM person
GROUP BY email
HAVING count(*) > 1;
