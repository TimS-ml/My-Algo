-- https://leetcode-cn.com/problems/consecutive-available-seats/

SELECT DISTINCT c1.seat_id
FROM cinema c1
JOIN cinema c2 ON abs(c1.seat_id - c2.seat_id) = 1
AND c1.free = 1
AND c2.free = 1
ORDER BY c1.seat_id;

-- select c1.seat_id
-- from cinema c1
-- left join cinema c2
-- on c1.seat_id + 1 = c2.seat_id
-- left join cinema c3
-- on c1.seat_id -1 = c3.seat_id
-- where (c1.free = 1 and c2.free = 1) or (c1.free = 1 and c3.free = 1)
-- order by 1