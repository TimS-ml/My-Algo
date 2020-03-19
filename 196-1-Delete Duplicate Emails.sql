-- https://leetcode-cn.com/problems/delete-duplicate-emails/

/*
create table Person (Id int, Email varchar(255));
insert into Person (Id, Email) values('1', 'john@example.com'), ('2', 'bob@example.com'), ('3', 'john@example.com');
*/

/* this will return bigger duplicate email
select p1.*
from Person p1,
    Person p2
where
    p1.Email = p2.Email and p1.Id > p2.Id;
*/

delete p1 from Person p1,
    Person p2
where
    p1.Email = p2.Email and p1.Id > p2.Id;
