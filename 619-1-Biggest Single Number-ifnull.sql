-- https://leetcode-cn.com/problems/biggest-single-number/
-- return null if nothing
 select
  (SELECT num
   FROM my_numbers
   GROUP BY num
   HAVING count(num) = 1
   ORDER BY num DESC
   LIMIT 1) AS num -- we can use ifnull instead, but slower

SELECT ifnull(
                (SELECT num
                 FROM my_numbers
                 GROUP BY num
                 HAVING count(num) = 1
                 ORDER BY num DESC
                 LIMIT 1), NULL) AS num