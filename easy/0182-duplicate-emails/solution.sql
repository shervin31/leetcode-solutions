SELECT p.email AS Email 
FROM Person p 
GROUP BY p.email 
HAVING COUNT(email) > 1 