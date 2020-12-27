-- https://leetcode-cn.com/problems/rising-temperature/
 -- select w1.Id as 'Id'
-- from weather w1
-- join weather w2
-- on DATEDIFF(w1.RecordDate, w2.RecordDate) = 1
-- and w1.Temperature > w2.Temperature;

SELECT w1.id AS 'Id'
FROM weather w1
JOIN weather w2 ON datediff(w1.recorddate, w2.recorddate) = 1
AND w1.temperature > w2.temperature;

