SELECT [firstname], [lastname] 
FROM [rider] 
GROUP BY [firstname], [lastname] 
HAVING COUNT(*) > 1 
ORDER BY [firstname], [lastname] 


SELECT * FROM rider ORDER BY [firstname], [lastname] 


SELECT * FROM [team]