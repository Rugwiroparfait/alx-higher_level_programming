#!/usr/bin/python3
"""module to list states from mySQL database"""
import sys
import MySQLdb

def list_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect (host='localhost', port=3306, user=username, db=database)
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    cursor.execute("Select * FROM states ORDER BY id ASC")

    # Fetch all the  rows from the query result
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)
    
    # Close the database
    db.close()

# Example Usage
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)