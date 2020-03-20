-- https://leetcode-cn.com/problems/consecutive-available-seats/

select distinct c1.seat_id from cinema c1, cinema c2
where abs(c1.seat_id - c2.seat_id) = 1
and c1.free and c2.free
order by c1.seat_id;