-- https://leetcode-cn.com/problems/biggest-single-number/
-- return null if nothing
 -- we can use ifnull instead

SELECT max(num) AS num
FROM
  (SELECT num
   FROM my_numbers
   GROUP BY num
   HAVING count(num) = 1) AS t