-- Display the max temperature of each state ordered
SELECT state, MAX(temperature) AS max_temperature
FROM city_temperatures
GROUP BY state
ORDER BY state;
