#!/usr/bin/python
"""Module that lists all states from the htbn database."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and search name from command-line arguments
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    #connect to MySQL server
    c = db.cursor()

    #execute the SQL query to retrieve all states
    c.execute ("SELECT `c`.`id;, `c`.`name`, `s`.`name` \
               FROM `cities` as `c` \
               INNER JOIN `states` as `s` \
               ON `c`.`states_id` =`s`.`d` \
               ORDER BY `c`.`id`")
    # Fetch all rows and print the states
    [print(city) for city in c.fetchall()]