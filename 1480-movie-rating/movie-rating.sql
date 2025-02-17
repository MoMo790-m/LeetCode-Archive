(SELECT name AS results
FROM movierating JOIN users USING(user_id)
GROUP BY name
ORDER BY COUNT(*) DESC,name
LIMIT 1)

UNION ALL

(SELECT title AS results
FROM movierating JOIN movies USING(movie_id)
WHERE movierating.created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY title
ORDER BY AVG(rating)DESC,title
LIMIT 1);