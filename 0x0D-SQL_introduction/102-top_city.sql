-- Display the top 3 cities
SELECT city, temperature
FROM city_temperatures
WHERE MONTH(date) IN (7, 8) -- Filter for July and August
ORDER BY temperature DESC
LIMIT 3;
