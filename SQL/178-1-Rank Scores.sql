-- https://leetcode-cn.com/problems/rank-scores/

SELECT scores.score,
       count(ranking.score) AS rank
FROM scores,

  (SELECT DISTINCT score
   FROM scores) ranking
WHERE scores.score <= ranking.score
GROUP BY scores.id,
         scores.score
ORDER BY scores.score DESC;