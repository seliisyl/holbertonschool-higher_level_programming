#!/usr/bin/env python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

def list_states(username, password, database):
    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the query to get all states
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all the results
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        list_states(username, password, database)
