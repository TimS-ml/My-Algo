-- https://leetcode-cn.com/problems/rising-temperature/

-- select w1.Id as 'Id'
-- from weather w1
-- join weather w2
-- on DATEDIFF(w1.RecordDate, w2.RecordDate) = 1
-- and w1.Temperature > w2.Temperature;


select w1.Id as 'Id'
from weather w1
join weather w2
on DATEDIFF(w1.RecordDate, w2.RecordDate) = 1
and w1.Temperature > w2.Temperature;
