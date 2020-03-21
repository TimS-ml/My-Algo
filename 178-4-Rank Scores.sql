-- https://leetcode-cn.com/problems/rank-scores/
-- Pre-uniqued version of ans3

select Score,
  (select count(*)
   from
     (select distinct Score s
      from Scores) tmp
   where s >= Score) Rank
from Scores
order by Score desc