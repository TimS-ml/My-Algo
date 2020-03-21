-- https://leetcode-cn.com/problems/rank-scores/

select Scores.Score,
       COUNT(Ranking.Score) as RANK
from Scores,
  (select distinct Score
   from Scores) Ranking
where Scores.Score <= Ranking.Score
group by Scores.Id,
         Scores.Score
order by Scores.Score desc;