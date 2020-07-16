-- https://leetcode-cn.com/problems/rank-scores/

SELECT s.score,
       count(DISTINCT t.score) rank
FROM scores s
JOIN scores t ON s.score <= t.score
GROUP BY s.id
ORDER BY s.score DESC