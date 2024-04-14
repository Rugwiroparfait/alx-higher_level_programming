#!/usr/bin/python3
""" displays all values in the states table of hbtn_0e_0_usa where name matches the argument."""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    # Connect to MYSQL server
    db =MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()


    # Execute the SQL query to retrieve all states sorted by id
    c.execute("SELECT * FROM 'states' ORDER BY 'id")
    [print(state) for state in c.fetchall () if state[1][0] == "N"]