-- https://leetcode-cn.com/problems/biggest-single-number/
-- return null if nothing

select(
    select num from my_numbers 
    group by num 
    having count(num) = 1 
    order by num desc 
    limit 1) as num

-- we can use ifnull instead, but slower
select ifnull((
    select num from my_numbers 
    group by num 
    having count(num) = 1 
    order by num desc 
    limit 1), null) as num

