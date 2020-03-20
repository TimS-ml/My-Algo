-- https://leetcode-cn.com/problems/biggest-single-number/
-- return null if nothing

-- we can use ifnull instead
select max(num) as num
from (select num from my_numbers
    group by num
    having count(num) = 1) as t
