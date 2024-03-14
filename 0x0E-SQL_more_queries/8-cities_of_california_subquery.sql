-- it lists all the cities of Calfonia that can be found in
-- htn_0d_usa.
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = "California"
);
