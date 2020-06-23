-- https://leetcode-cn.com/problems/rising-temperature/

SELECT w1.id
FROM weather w1
INNER JOIN weather w2 ON to_days(w1.recorddate) = to_days(w2.recorddate) + 1
WHERE w1.temperature > w2.temperature -- or: TO_DAYS(w1.RecordDate)-TO_DAYS(w2.RecordDate) = 1