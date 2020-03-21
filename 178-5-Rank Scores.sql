-- https://leetcode-cn.com/problems/rank-scores/

select s.Score,
       count(distinct t.score) Rank
from Scores s
join Scores t on s.Score <= t.score
group by s.Id
order by s.Score desc