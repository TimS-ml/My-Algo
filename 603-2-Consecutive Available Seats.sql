-- https://leetcode-cn.com/problems/consecutive-available-seats/

SELECT DISTINCT c1.seat_id
FROM cinema c1,
     cinema c2
WHERE abs(c1.seat_id - c2.seat_id) = 1
  AND c1.free
  AND c2.free
ORDER BY c1.seat_id;