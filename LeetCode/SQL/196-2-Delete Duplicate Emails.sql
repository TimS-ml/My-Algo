-- https://leetcode-cn.com/problems/delete-duplicate-emails/
 /*
create table Person (Id int, Email varchar(255));
insert into Person (Id, Email) values('1', 'john@example.com'), ('2', 'bob@example.com'), ('3', 'john@example.com');
*/ -- This will return 1 and 2 in text case
-- select min(Id) as Id from Person group by Email;

DELETE
FROM person
WHERE id NOT IN
    (SELECT min(id) AS id
     FROM person
     GROUP BY email)