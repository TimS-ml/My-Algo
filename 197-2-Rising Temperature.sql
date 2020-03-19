-- https://leetcode-cn.com/problems/rising-temperature/

select w1.Id
from Weather w1
inner join Weather w2
on TO_DAYS(w1.RecordDate) = TO_DAYS(w2.RecordDate) + 1
where w1.Temperature > w2.Temperature

-- or: TO_DAYS(w1.RecordDate)-TO_DAYS(w2.RecordDate) = 1