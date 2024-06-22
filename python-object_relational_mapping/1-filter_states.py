#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from the
database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def list_states_starting_with_N(username, password, database):
    try:
        # Connect to the database
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database)
        cursor = db.cursor()

        # Execute the query to get all states with a name starting with 'N'
        query = ("SELECT id, name FROM states WHERE name LIKE 'N%' "
                 "ORDER BY id ASC")
        cursor.execute(query)

        # Fetch all the results
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close the cursor and the connection
        cursor.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        list_states_starting_with_N(username, password, database)
    else:
        print("Usage: python3 1-filter_states.py <username> <password> "
              "<database>")
