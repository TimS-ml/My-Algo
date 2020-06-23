-- https://leetcode-cn.com/problems/duplicate-emails/
-- check question 196

SELECT email
FROM person
GROUP BY email
HAVING count(*) > 1;