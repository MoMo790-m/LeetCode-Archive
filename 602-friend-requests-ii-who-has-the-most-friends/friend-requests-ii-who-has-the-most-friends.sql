WITH a as 
(SELECT requester_id AS id FROM RequestAccepted
UNION ALL 
SELECT accepter_id AS id FROM RequestAccepted)

SELECT id,COUNT(id) AS num
FROM a
GROUP BY id
ORDER BY num DESC
LIMIT 1;
