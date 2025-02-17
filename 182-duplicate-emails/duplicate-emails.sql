SELECT DISTINCT email "Email"
FROM person 
GROUP BY email
HAVING COUNT(email) > 1

 
