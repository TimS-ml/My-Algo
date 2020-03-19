-- https://leetcode-cn.com/problems/duplicate-emails/
-- check question 196

select Email
from Person
group by Email
having count(*) > 1;