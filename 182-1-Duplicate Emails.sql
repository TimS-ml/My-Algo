-- https://leetcode-cn.com/problems/duplicate-emails/
-- check question 196

SELECT email
FROM
  (SELECT email,
          count(email) AS num
   FROM person
   GROUP BY email) AS statistic
WHERE num > 1;