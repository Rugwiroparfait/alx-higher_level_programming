-- calculate the average temperature
SELECT city, AVG(temperature) AS average_temperature_fahrenheit
FROM city_temperatures
GROUP BY city
ORDER BY average_temperature_fahrenheit DESC;
